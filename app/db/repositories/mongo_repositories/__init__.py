from typing import Optional, Any, Dict

from bson import ObjectId
from pydantic import BaseModel
from pymongo.client_session import ClientSession

from app import db
from app.db.exceptions import PersistenceExceptionFactory
from app.db.repositories.interfaces import IBasicRepository, IStandardRepository


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


class MongoQueryProjectionGenerator:
    def element_match_rec(self, value: Any) -> Any:
        if isinstance(value, list):
            return {"$all": [self.element_match_rec(item) for item in value]}
        elif isinstance(value, dict):
            return {k: self.element_match_rec(v) for k, v in value.items()}
        else:
            return value

    def element_match(self, element: Any) -> Dict:
        if isinstance(element, dict):
            return {"$elemMatch": self.element_match_rec(element)}
        else:
            return element

    def query(self, id: Optional[str] = None,
              has_attribute: Optional[list[str]] = None,
              does_not_have_attribute: Optional[list[str]] = None,
              has_attribute_value: Optional[dict] = None,
              has_list_value: Optional[dict] = None) -> dict:
        query = dict()
        if id:
            query["_id"] = ObjectId(id)
        if has_attribute:
            for attribute in has_attribute:
                query[attribute] = {"$exists": True}
        if does_not_have_attribute:
            for attribute in does_not_have_attribute:
                query[attribute] = {"$exists": False}
        if has_attribute_value:
            for attribute, value in has_attribute_value.items():
                query[attribute] = value
        if has_list_value:
            for attribute, value in has_list_value.items():
                query[attribute] = self.element_match(value)
        return query

    @staticmethod
    def projection(id: Optional[bool] = None,
                   include_projection_attribute: Optional[list[str]] = None,
                   exclude_projection_attribute: Optional[list[str]] = None) -> dict:
        projection = dict()
        if include_projection_attribute and exclude_projection_attribute:
            raise Exception("Forbidden include and exclude projection at the same time.")
        if include_projection_attribute is None:
            include_projection_attribute = []
        if exclude_projection_attribute is None:
            exclude_projection_attribute = []
        if id is True:
            include_projection_attribute.append("_id")
        elif id is False:
            exclude_projection_attribute.append("_id")
        if include_projection_attribute:
            for attribute in include_projection_attribute:
                projection[attribute] = True
        if exclude_projection_attribute:
            for attribute in exclude_projection_attribute:
                projection[attribute] = False
        return projection


class BasicMongoRepository(IBasicRepository):
    def __init__(self, collection: str):
        self.collection = collection
        self.exception_factory = PersistenceExceptionFactory(collection)
        self.generator = MongoQueryProjectionGenerator()

    def _get_db(self):
        return db.get_collection(self.collection)

    def get_all(self, session: Optional[ClientSession] = None):
        return self._get_db().find(session=session)

    def get(self, id: str, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            self.generator.query(id),
            session=session)
        if result is None:
            raise self.exception_factory.document_not_found(id)
        return result

    def exists(self, id: str, session: Optional[ClientSession] = None):
        result = self._get_db().find_one(
            self.generator.query(id),
            self.generator.projection(id=True),
            session=session)
        if result is None:
            return False
        return True

    def create(self, document, session: Optional[ClientSession] = None) -> str:
        result = self._get_db().insert_one(document, session=session)
        return str(result.inserted_id)

    def delete(self, id: str, session: Optional[ClientSession] = None):
        result = self._get_db().delete_one(
            self.generator.query(id),
            session=session)
        if result.deleted_count != 1:
            raise self.exception_factory.document_not_found(id)


class MongoStandardRepository(BasicMongoRepository, IStandardRepository):
    def __init__(self, collection: str):
        super().__init__(collection)

    def get_all_with_query_and_projection(self,
                                          has_attribute: Optional[list[str]] = None,
                                          does_not_have_attribute: Optional[list[str]] = None,
                                          has_attribute_value: Optional[dict] = None,
                                          has_list_value: Optional[dict] = None,
                                          include_projection_attribute: Optional[list[str]] = None,
                                          exclude_projection_attribute: Optional[list[str]] = None,
                                          id_projection: Optional[bool] = None,
                                          session: Optional[ClientSession] = None) -> Any:
        result = self._get_db().find(
            self.generator.query(
                has_attribute = has_attribute,
                does_not_have_attribute = does_not_have_attribute,
                has_attribute_value = has_attribute_value,
                has_list_value = has_list_value),
            self.generator.projection(id=id_projection, include_projection_attribute=include_projection_attribute,
                                      exclude_projection_attribute=exclude_projection_attribute),
            session=session)
        return result

    def get_with_query_and_projection(self,
                                      has_attribute: Optional[list[str]] = None,
                                      does_not_have_attribute: Optional[list[str]] = None,
                                      has_attribute_value: Optional[dict] = None,
                                      has_list_value: Optional[dict] = None,
                                      include_projection_attribute: Optional[list[str]] = None,
                                      exclude_projection_attribute: Optional[list[str]] = None,
                                      id_projection: Optional[bool] = None,
                                      session: Optional[ClientSession] = None) -> Any:
        result = self._get_db().find_one(
            self.generator.query(
                has_attribute=has_attribute,
                does_not_have_attribute=does_not_have_attribute,
                has_attribute_value=has_attribute_value,
                has_list_value=has_list_value),
            self.generator.projection(id_projection, include_projection_attribute, exclude_projection_attribute),
            session=session)
        return result

    def get_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None) -> Any:
        result = self._get_db().find_one(
            self.generator.query(id),
            self.generator.projection(include_projection_attribute=[attribute]),
            session=session)
        if result is None:
            raise self.exception_factory.document_not_found(id)
        if attribute not in result:
            raise self.exception_factory.field_not_found(id, attribute)
        return result[attribute]

    def set_attribute(self, id: str, attribute: str, value, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            self.generator.query(id),
            {"$set": {attribute: value}},
            session=session)
        if result.matched_count <= 0:
            raise self.exception_factory.document_not_found(id)
        if result.modified_count <= 0:
            raise self.exception_factory.field_already_exists(id, attribute)

    def unset_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            self.generator.query(id),
            {"$unset": {attribute: ""}},
            session=session)
        if result.matched_count <= 0:
            raise self.exception_factory.document_not_found(id)
        if result.modified_count <= 0:
            raise self.exception_factory.field_not_found(id, attribute)

    def push_to_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            self.generator.query(id),
            {"$push": {attribute: element}},
            session=session)
        if result.matched_count <= 0:
            raise self.exception_factory.document_not_found(id)
        if result.modified_count <= 0:
            raise self.exception_factory.operation_failed(id, attribute)

    def pull_from_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None):
        result = self._get_db().update_one(
            self.generator.query(id),
            {"$pull": {attribute: element}},
            session=session)
        if result.matched_count <= 0:
            raise self.exception_factory.document_not_found(id)
        if result.modified_count <= 0:
            raise self.exception_factory.operation_failed(id, attribute)

    def get_from_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None) -> Any:
        result = self._get_db().find_one(
            {"_id": ObjectId(id), attribute: self.generator.element_match(element)},
            {f"{attribute}.$": True},
            session=session)
        if not result:
            raise self.exception_factory.document_not_found(id)
        if attribute not in result or not result[attribute]:
            raise self.exception_factory.field_does_not_match(id, attribute, element)
        return result[attribute][0]

    def has_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None) -> bool:
        result = self._get_db().find_one(self.generator.query(id=id, has_attribute=[attribute]))
        if not result:
            return False
        return True

    def has_element_in_list_attribute(self, id: str, attribute: str, element,
                                      session: Optional[ClientSession] = None) -> bool:
        result = self._get_db().find_one(
            {"_id": ObjectId(id), attribute: self.generator.element_match(element)},
            {f"{attribute}.$": True},
            session=session)
        if not result or attribute not in result or len(result[attribute]) == 0:
            return False
        return True
