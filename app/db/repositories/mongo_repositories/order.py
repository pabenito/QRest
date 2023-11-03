from typing import Optional

from app.core.entities.order import OrderPost, Element, Command, ReceiptElement
from app.db.entities.order import VersionedOrder
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository


class MongoOrderRepository(IOrderRepository):
    def __init__(self):
        self.repository = MongoStandardRepository("order")

    def create(self, order: OrderPost) -> str:
        new_order = VersionedOrder(**order.model_dump())
        return self.repository.create(new_order.model_dump())

    def delete(self, order_id: str):
        self.repository.delete(order_id)

    def get_current_command(self, order_id: str) -> list[Element]:
        return self.repository.get_attribute(order_id, "current_command")

    def delete_current_command(self, order_id: str):
        return self.repository.unset_attribute(order_id, "current_command")

    def get_commands(self, order_id: str) -> list[Command]:
        return self.repository.get_attribute(order_id, "commands")

    def add_command(self, order_id: str, command: Command):
        return self.repository.push_attribute(order_id, "commands", command)

    def get_receipt(self, order_id: str) -> list[ReceiptElement]:
        return self.repository.get_attribute(order_id, "receipt")

    def set_receipt(self, order_id: str, receipt: list[ReceiptElement]):
        return self.repository.set_attribute(order_id, "receipt", receipt)
