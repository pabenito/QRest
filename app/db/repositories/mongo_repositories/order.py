from typing import Type, Any, Tuple

from app.db import db
from app.db.repositories.interfaces.order import IOrderRepository


class MongoOrderRepository(IOrderRepository):
    def __init__(self):
        self.db = db["order"]

    def get_attribute(self, order: str, attribute_name: str, attribute_type: Type[Any]) -> Tuple[int, Type[Any]]:
        pass

    def add_attribute(self, order: str, version: int, attribute_name: str, attribute):
        pass

    def remove_attribute(self, order: str, version: int, attribute_name: str):
        pass
