from typing import Optional

from pymongo.client_session import ClientSession

from app.core.entities.order import OrderPost, Element, Command, ReceiptElement
from app.db.entities.order import VersionedOrder
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository


class MongoOrderRepository(IOrderRepository):
    def __init__(self):
        self.repository = MongoStandardRepository("order")

    def create(self, order: OrderPost, session: Optional[ClientSession] = None) -> str:
        new_order = VersionedOrder(**order.model_dump())
        return self.repository.create(new_order.model_dump(), session)

    def delete(self, order_id: str, session: Optional[ClientSession] = None):
        self.repository.delete(order_id, session)

    def get_current_command(self, order_id: str, session: Optional[ClientSession] = None) -> list[Element]:
        return self.repository.get_attribute(order_id, "current_command", session)

    def delete_current_command(self, order_id: str, session: Optional[ClientSession] = None):
        return self.repository.unset_attribute(order_id, "current_command", session)

    def get_commands(self, order_id: str, session: Optional[ClientSession] = None) -> list[Command]:
        return self.repository.get_attribute(order_id, "commands", session)

    def add_command(self, order_id: str, command: Command, session: Optional[ClientSession] = None):
        return self.repository.push_to_list_attribute(order_id, "commands", command, session)

    def get_receipt(self, order_id: str, session: Optional[ClientSession] = None) -> list[ReceiptElement]:
        return self.repository.get_attribute(order_id, "receipt", session)

    def set_receipt(self, order_id: str, receipt: list[ReceiptElement], session: Optional[ClientSession] = None):
        return self.repository.set_attribute(order_id, "receipt", receipt)
