from typing import Type, Any, Tuple

from app.core.entities.order import Order, OrderPost, Element, Command, ReceiptElement
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

    def get_version(self, order: str) -> int:
        pass

    def get_current_command(self, order_id: str) -> list[Element]:
        pass

    def delete_current_command(self, order_id: str):
        pass

    def get_commands(self, order_id: str) -> list[Command]:
        pass

    def add_command(self, order_id: str, command: Command):
        pass

    def get_receipt(self, order_id: str) -> list[ReceiptElement]:
        pass

    def set_receipt(self, order_id: str, receipt: list[ReceiptElement]):
        pass
