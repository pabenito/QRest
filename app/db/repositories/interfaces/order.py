from typing import Type, Any, Tuple, Optional

from app.core.entities.order import Order, OrderPost


class IOrderRepository:
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
