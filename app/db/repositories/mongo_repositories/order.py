from typing import Optional

from app.core.entities.order import OrderPost, Element, Command, ReceiptElement
from app.db.entities.order import VersionedOrder
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository, MongoOCCRepository, OptionalOCCRepository


class MongoOrderRepository(IOrderRepository):
    def __init__(self):
        self.repository = OptionalOCCRepository(
            standard_repository=MongoStandardRepository("order"),
            occ_repository=MongoOCCRepository("order"))

    def create(self, order: OrderPost) -> str:
        new_order = VersionedOrder(**order.model_dump())
        return self.repository.create(new_order.model_dump())

    def delete(self, order_id: str):
        self.repository.delete(order_id)

    def get_version(self, order_id: str) -> int:
        return self.repository.get_version(order_id)

    def get_current_command(self, order_id: str, version: Optional[int] = None) -> list[Element]:
        return self.repository.get_attribute(order_id, "current_command", version)

    def delete_current_command(self, order_id: str, version: Optional[int] = None):
        return self.repository.unset_attribute(order_id, "current_command", version)

    def get_commands(self, order_id: str, version: Optional[int] = None) -> list[Command]:
        return self.repository.get_attribute(order_id, "commands", version)

    def add_command(self, order_id: str, command: Command, version: Optional[int] = None):
        return self.repository.push_attribute(order_id, "commands", command, version)

    def get_receipt(self, order_id: str, version: Optional[int] = None) -> list[ReceiptElement]:
        return self.repository.get_attribute(order_id, "receipt", version)

    def set_receipt(self, order_id: str, receipt: list[ReceiptElement], version: Optional[int] = None):
        return self.repository.set_attribute(order_id, "receipt", receipt, version)
