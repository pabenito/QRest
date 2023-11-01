from bson import ObjectId

from app import db
from app.core.exceptions import ResourceNotFoundException, OperationFailedException


class MongoRepository:
    def __init__(self, collection: str):
        self.collection = collection

    def _exception_not_found(self, id: str) -> ResourceNotFoundException:
        return ResourceNotFoundException(self.collection, "id", id)

    def _exception_operation_failed(self, message: str) -> OperationFailedException:
        return OperationFailedException(self.collection, message)

    def _get_db(self):
        return db.get_collection(self.collection)

    def insert_one(self, document) -> str:
        result = self._get_db().insert_one(document)
        return str(result.inserted_id)

    def delete_one(self, id: str):
        result = self._get_db().delete_one({"_id": ObjectId(id)})
        if result.deleted_count != 1:
            raise self._exception_not_found(id)

    def get_attribute(self, id: str, attribute: str):
        result = self._get_db().find_one({"_id": ObjectId()}, {attribute: True})
        if result is None:
            raise self._exception_not_found(id)
        return result[attribute]

    def set_attribute(self, id: str, attribute: str, value):
        result = self._get_db().update_one({"_id": ObjectId(id)}, {"$set": {attribute: value}})
        if result.matched_count <= 0:
            raise self._exception_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error setting attribute. Order with id {id} already has {attribute} value: {value}")

    def unset_attribute(self, id: str, attribute: str):
        result = self._get_db().update_one({"_id": ObjectId(id)}, {"$unset": {attribute: ""}})
        if result.matched_count <= 0:
            raise self._exception_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error unsetting attribute. Order with id {id} does not have '{attribute}' attribute")

    def push_attribute(self, id: str, attribute: str, value):
        result = self._get_db().update_one({"_id": ObjectId(id)}, {"$push": {attribute: value}})
        if result.matched_count <= 0:
            raise self._exception_not_found(id)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error pushing attribute. Order with id {id} attribute '{attribute}' with value: {value}")

    def pop_attribute(self, id: str, attribute: str, last=True):
        index = 1 if last else -1
        result = self._get_db().update_one({"_id": ObjectId(id)}, {"$pop": {attribute: index}})
        if result.matched_count <= 0:
            raise self._exception_not_found(id)
        if result.modified_count <= 0:
            position = "last" if last else "first"
            raise self._exception_operation_failed(
                f"Error popping attribute. Order with id {id} attribute '{attribute}' popping {position}")
