from typing import Optional
from bson import ObjectId
from pymongo.client_session import ClientSession

from app import db
from app.db.repositories.interfaces import IBasicRepository, IStandardRepository, IOCCRepository, IOptionalOCCRepository
from app.core.exceptions import ResourceNotFoundException, OperationFailedException, ConcurrencyCollisionException


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

    def _exception_not_found(self, id: str) -> ResourceNotFoundException:
        return ResourceNotFoundException(self.collection, "id", id)

    def _exception_operation_failed(self, message: str) -> OperationFailedException:
        return OperationFailedException(self.collection, message)

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
            raise self._exception_not_found(id)

    def get(self, id: str, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            {"_id": ObjectId(id)},
            session=session)
        if result is None:
            raise self._exception_not_found(id)
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

    def get_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            {"_id": ObjectId()},
            {attribute: True},
            session=session)
        if result is None:
            raise self._exception_not_found(id)
        return result[attribute]

    def set_attribute(self, id: str, attribute: str, value, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            {"_id": ObjectId(id)},
            {"$set": {attribute: value}},
            session=session)
        if result.matched_count <= 0:
            raise self._exception_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error setting attribute. Order with id {id} already has {attribute} value: {value}")

    def unset_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            {"_id": ObjectId(id)},
            {"$unset": {attribute: ""}},
            session=session)
        if result.matched_count <= 0:
            raise self._exception_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error unsetting attribute. Order with id {id} does not have '{attribute}' attribute")

    def push_to_list_attribute(self, id: str, attribute: str, value, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            {"_id": ObjectId(id)},
            {"$push": {attribute: value}},
            session=session)
        if result.matched_count <= 0:
            raise self._exception_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error pushing attribute. Order with id {id} attribute '{attribute}' with value: {value}")

    def pull_from_list_attribute(self, id: str, attribute: str, match: dict, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            {"_id": ObjectId(id)},
            {"$pull": {attribute: match}},
            session=session)
        if result.matched_count <= 0:
            raise self._exception_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error pulling attribute. Order with id {id} attribute '{attribute}' pulling {match}")

    def get_from_list_attribute(self, id: str, attribute: str, match: dict, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            {"_id": ObjectId(id), attribute: {"$elemMatch": match}},
            {f"{attribute}.$": True},
            session=session)
        if not result:
            raise self._exception_not_found(id)
        if attribute not in result or len(result[attribute]) == 0:
            raise self._exception_operation_failed(f"There is no element that match: {match}")
        return result[attribute][0]
