from typing import Type, Any

from app.core.entities.order import Order


class IOrderRepository:
    def get_attribute(self, order: str, attribute_name: str, attribute_type: Type[Any]):
        pass

    def add_attribute(self, order: str, attribute_name: str, attribute):
        pass

    def remove_attribute(self, order: str, attribute_name: str, attribute):
        pass
