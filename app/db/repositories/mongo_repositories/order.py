from typing import Type, Any, Tuple

from app.core.entities.order import Order, OrderPost
from app import db
from app.db.repositories.interfaces.order import IOrderRepository


class MongoOrderRepository(IOrderRepository):
    @staticmethod
    def _get_db():
        return db.get_collection("order")

    def create(self, order: OrderPost) -> str:
        pass

    def delete(self, order: str) -> Order:
        pass

    def get_attribute(self, order: str, attribute_name: str, attribute_type: Type[Any]) -> Tuple[int, Type[Any]]:
        pass

    def add_attribute(self, order: str, version: int, attribute_name: str, attribute):
        pass

    def remove_attribute(self, order: str, version: int, attribute_name: str):
        pass
