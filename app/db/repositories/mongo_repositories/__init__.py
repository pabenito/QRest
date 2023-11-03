from typing import Optional, Any, Dict
from bson import ObjectId
from pydantic import BaseModel
from pymongo.client_session import ClientSession

from app import db
from app.db.repositories.interfaces import IBasicRepository, IStandardRepository
from app.core.exceptions import DocumentNotFoundException, OperationFailedException, FieldNotFoundException, \
    FieldAlreadyExistsException, FieldDoesNotMatchException


class MongoTransactionManager:
    def __init__(self):
        self.client = db.get_client()

    def __enter__(self):
        self.session = self.client.start_session()
        self.session.start_transaction()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.abort_transaction()
        else:
            self.session.commit_transaction()
        self.session.end_session()


class BasicMongoRepository(IBasicRepository):
    def __init__(self, collection: str):
        self.collection = collection

    def _exception_document_not_found(self, id: str) -> DocumentNotFoundException:
        return DocumentNotFoundException(self.collection, "id", id)
    
    def _exception_field_not_found(self, id: str, field: str) -> FieldNotFoundException:
        return FieldNotFoundException(self.collection, "id", id, field)

    def _exception_field_does_not_match(self, id: str, field: str, value: str) -> FieldDoesNotMatchException:
        return FieldDoesNotMatchException(self.collection, "id", id, field, value)

    def _exception_field_already_exists(self, id: str, field: str) -> FieldAlreadyExistsException:
        return FieldAlreadyExistsException(self.collection, "id", id, field)

    def _exception_operation_failed(self, id: str, field: Optional[str]) -> OperationFailedException:
        return OperationFailedException(self.collection, "id", id, field)

    def _get_db(self):
        return db.get_collection(self.collection)

    def create(self, document, session: Optional[ClientSession] = None) -> str:
        result = self._get_db().insert_one(document, session=session)
        return str(result.inserted_id)

    def delete(self, id: str, session: Optional[ClientSession] = None):
        result = self._get_db().delete_one(
            {"_id": ObjectId(id)},
            session=session)
        if result.deleted_count != 1:
            raise self._exception_document_not_found(id)

    def get(self, id: str, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            {"_id": ObjectId(id)},
            session=session)
        if result is None:
            raise self._exception_document_not_found(id)
        return result

    def exists(self, id: str, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            {"_id": ObjectId()},
            {"_id": True},
            session=session)
        if result is None:
            return False
        return True


class MongoStandardRepository(IStandardRepository, BasicMongoRepository):
    def __init__(self, collection: str):
        super().__init__(collection)
        
    def _generate_query_rec(self, value: Any) -> Any:
        if isinstance(value, list):
            return {"$all": [self._generate_query_rec(item) for item in value]}
        elif isinstance(value, BaseModel):
            return {k: self._generate_query_rec(v) for k, v in value.model_dump().items()}
        elif isinstance(value, dict):
            return {k: self._generate_query_rec(v) for k, v in value.items()}
        else:
            return value

    def _generate_query(self, element: Any) -> Dict:
        if isinstance(element, (BaseModel, dict)):
            return {"$elemMatch": self._generate_query_rec(element)}
        else:
            return element

    def get_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            {"_id": ObjectId()},
            {attribute: True},
            session=session)
        if result is None:
            raise self._exception_document_not_found(id)
        if attribute not in result:
            raise self._exception_field_not_found(id, attribute)
        return result[attribute]

    def set_attribute(self, id: str, attribute: str, value, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            {"_id": ObjectId(id)},
            {"$set": {attribute: value}},
            session=session)
        if result.matched_count <= 0:
            raise self._exception_document_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_field_already_exists(id, attribute)

    def unset_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            {"_id": ObjectId(id)},
            {"$unset": {attribute: ""}},
            session=session)
        if result.matched_count <= 0:
            raise self._exception_document_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_field_not_found(id, attribute)

    def push_to_list_attribute(self, id: str, attribute: str, value, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            {"_id": ObjectId(id)},
            {"$push": {attribute: value}},
            session=session)
        if result.matched_count <= 0:
            raise self._exception_document_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(id, attribute)

    def pull_from_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            {"_id": ObjectId(id)},
            {"$pull": {attribute: self._generate_query(element)}},
            session=session)
        if result.matched_count <= 0:
            raise self._exception_document_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(id, attribute)

    def get_from_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            {"_id": ObjectId(id), attribute: self._generate_query(element)},
            {f"{attribute}.$": True},
            session=session)
        if not result:
            raise self._exception_document_not_found(id)
        if attribute not in result or not result[attribute]:
            raise self._exception_field_does_not_match(id, attribute, element)
        return result[attribute][0]

    def has_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None) -> bool:
        result = self._get_db().find_one({"_id": ObjectId(id), attribute: {"$exists": True}})
        if not result:
            return False
        return True

    def has_element_in_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None) -> bool:
        result = self._get_db().find_one(
            {"_id": ObjectId(id), attribute: self._generate_query(element)},
            {f"{attribute}.$": True},
            session=session)
        if not result or attribute not in result or len(result[attribute]) == 0:
            return False
        return True
