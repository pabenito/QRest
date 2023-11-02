from typing import Optional

from bson import ObjectId

from app import db
from app.core.exceptions import ResourceNotFoundException, OperationFailedException, ConcurrencyCollisionException


class IBasicRepository:
    def exists(self, id: str):
        pass

    def insert_one(self, document) -> str:
        pass

    def delete_one(self, id: str):
        pass


class IStandardRepository(IBasicRepository):
    def get_attribute(self, id: str, attribute: str):
        pass

    def set_attribute(self, id: str, attribute: str, value):
        pass

    def unset_attribute(self, id: str, attribute: str):
        pass

    def push_attribute(self, id: str, attribute: str, value):
        pass

    def pop_attribute(self, id: str, attribute: str, last=True):
        pass


class IOCCRepository(IBasicRepository):
    def get_version(self, id: str) -> int:
        pass

    def get_attribute(self, id: str, attribute: str, version: int):
        pass

    def set_attribute(self, id: str, attribute: str, value, version: int):
        pass

    def unset_attribute(self, id: str, attribute: str, version: int):
        pass

    def push_attribute(self, id: str, attribute: str, value, version: int):
        pass

    def pop_attribute(self, id: str, attribute: str, version: int, last=True):
        pass


class IOptionalOCCRepository(IBasicRepository):
    def get_version(self, id: str) -> int:
        pass

    def get_attribute(self, id: str, attribute: str, version: Optional[int] = None):
        pass

    def set_attribute(self, id: str, attribute: str, value, version: Optional[int] = None):
        pass

    def unset_attribute(self, id: str, attribute: str, version: Optional[int] = None):
        pass

    def push_attribute(self, id: str, attribute: str, value, version: Optional[int] = None):
        pass

    def pop_attribute(self, id: str, attribute: str, last=True, version: Optional[int] = None):
        pass
