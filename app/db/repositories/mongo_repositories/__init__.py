from typing import Optional
from bson import ObjectId

from app import db
from app.db.repositories.interfaces import IBasicRepository, IStandardRepository, IOCCRepository, IOptionalOCCRepository
from app.core.exceptions import ResourceNotFoundException, OperationFailedException, ConcurrencyCollisionException


class BasicMongoRepository(IBasicRepository):
    def __init__(self, collection: str):
        self.collection = collection

    def _exception_not_found(self, id: str) -> ResourceNotFoundException:
        return ResourceNotFoundException(self.collection, "id", id)

    def _exception_operation_failed(self, message: str) -> OperationFailedException:
        return OperationFailedException(self.collection, message)

    def _get_db(self):
        return db.get_collection(self.collection)

    def create(self, document) -> str:
        result = self._get_db().insert_one(document)
        return str(result.inserted_id)

    def delete(self, id: str):
        result = self._get_db().delete_one({"_id": ObjectId(id)})
        if result.deleted_count != 1:
            raise self._exception_not_found(id)

    def get(self, id: str):
        result = self._get_db().find_one({"_id": ObjectId(id)})
        if result is None:
            raise self._exception_not_found(id)
        return result

    def exists(self, id: str):
        result = self._get_db().find_one({"_id": ObjectId()}, {"_id": True})
        if result is None:
            return False
        return True


class MongoStandardRepository(IStandardRepository, BasicMongoRepository):
    def __init__(self, collection: str):
        super().__init__(collection)

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


class MongoOCCRepository(IOCCRepository, BasicMongoRepository):
    def __init__(self, collection: str):
        super().__init__(collection)

    def _exception_concurrency_collision(self, id: str, method: str,
                                         expected_version: int) -> ConcurrencyCollisionException:
        return ConcurrencyCollisionException(self.collection, id, method, expected_version)

    def get_version(self, id: str) -> int:
        if not self.exists(id):
            raise self._exception_not_found(id)
        return self.get_attribute(id, "version")

    def get_attribute(self, id: str, attribute: str, version: int):
        if not self.exists(id):
            raise self._exception_not_found(id)
        result = self._get_db().find_one({"_id": ObjectId(id), "version": version}, {attribute: True})
        if result is None:
            raise self._exception_concurrency_collision(id, "get_attribute", version)
        return result[attribute]

    def set_attribute(self, id: str, attribute: str, value, version: int):
        if not self.exists(id):
            raise self._exception_not_found(id)
        result = self._get_db().update_one({"_id": ObjectId(id), "version": version},
                                           {"$set": {"version": version + 1, attribute: value}})
        if result.matched_count <= 0:
            raise self._exception_concurrency_collision(id, "set_attribute", version)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error setting attribute. Order with id {id} already has {attribute} value: {value}")

    def unset_attribute(self, id: str, attribute: str, version: int):
        if not self.exists(id):
            raise self._exception_not_found(id)
        result = self._get_db().update_one({"_id": ObjectId(id), "version": version},
                                           {"$set": {"version": version + 1},
                                            "$unset": {attribute: ""}})
        if result.matched_count <= 0:
            raise self._exception_concurrency_collision(id, "unset_attribute", version)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error unsetting attribute. Order with id {id} does not have '{attribute}' attribute")

    def push_attribute(self, id: str, attribute: str, value, version: int):
        if not self.exists(id):
            raise self._exception_not_found(id)
        result = self._get_db().update_one({"_id": ObjectId(id), "version": version},
                                           {"$set": {"version": version + 1},
                                            "$push": {attribute: value}})
        if result.matched_count <= 0:
            raise self._exception_concurrency_collision(id, "push_attribute", version)
        if result.modified_count <= 0:
            raise self._exception_operation_failed(
                f"Error pushing attribute. Order with id {id} attribute '{attribute}' with value: {value}")

    def pop_attribute(self, id: str, attribute: str, version: int, last=True):
        if not self.exists(id):
            raise self._exception_not_found(id)
        index = 1 if last else -1
        result = self._get_db().update_one({"_id": ObjectId(id), "version": version},
                                           {"$set": {"version": version + 1},
                                            "$pop": {attribute: index}})
        if result.matched_count <= 0:
            raise self._exception_concurrency_collision(id, "pop_attribute", version)
        if result.modified_count <= 0:
            position = "last" if last else "first"
            raise self._exception_operation_failed(
                f"Error popping attribute. Order with id {id} attribute '{attribute}' popping {position}")


class OptionalOCCRepository(IOptionalOCCRepository):
    def __init__(self, standard_repository: MongoStandardRepository, occ_repository: IOCCRepository):
        self.standard_repository = standard_repository
        self.occ_repository = occ_repository

    def create(self, document) -> str:
        return self.standard_repository.create(document)

    def delete(self, id: str):
        return self.standard_repository.delete(id)

    def get(self, id: str):
        return self.standard_repository.get(id)

    def exists(self, id: str):
        return self.standard_repository.exists(id)

    def get_version(self, id: str) -> int:
        return self.occ_repository.get_version(id)

    def get_attribute(self, id: str, attribute: str, version: Optional[int] = None):
        if version:
            return self.occ_repository.get_attribute(id, attribute, version)
        return self.standard_repository.get_attribute(id, attribute)

    def set_attribute(self, id: str, attribute: str, value, version: Optional[int] = None):
        if version:
            return self.occ_repository.set_attribute(id, attribute, value, version)
        return self.standard_repository.set_attribute(id, attribute, value)

    def unset_attribute(self, id: str, attribute: str, version: Optional[int] = None):
        if version:
            return self.occ_repository.unset_attribute(id, attribute, version)
        return self.standard_repository.unset_attribute(id, attribute)

    def push_attribute(self, id: str, attribute: str, value, version: Optional[int] = None):
        if version:
            return self.occ_repository.push_attribute(id, attribute, value, version)
        return self.standard_repository.push_attribute(id, attribute, value)

    def pop_attribute(self, id: str, attribute: str, last=True, version: Optional[int] = None):
        if version:
            return self.occ_repository.pop_attribute(id, attribute, version, last)
        return self.standard_repository.pop_attribute(id, attribute, last)
