from typing import Optional
from pymongo.client_session import ClientSession

from app.core.entities.order import OrderPost, Element, Command, ReceiptElement
from app.db.repositories.interfaces import IStandardRepository
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.lib.utils import parse_object, json_lower_encoder


class MongoOrderRepository(IOrderRepository):
    def __init__(self):
        self.repository: IStandardRepository = MongoStandardRepository("orders")
        self.encoder = json_lower_encoder
        self.parse = parse_object

    def create(self, order: OrderPost, session: Optional[ClientSession] = None) -> str:
        return self.repository.create(self.encoder(order), session)

    def delete(self, order_id: str, session: Optional[ClientSession] = None):
        self.repository.delete(order_id, session)

    def exists(self, order_id: str, session: Optional[ClientSession] = None) -> bool:
        return self.repository.exists(order_id, session)

    def has_current_command(self, order_id: str, session: Optional[ClientSession] = None) -> bool:
        return self.repository.has_attribute(order_id, "current_command", session)

    def get_current_command(self, order_id: str, session: Optional[ClientSession] = None) -> list[Element]:
        result = self.repository.get_attribute(order_id, "current_command", session)
        return self.parse(list(result), list[Element])

    def delete_current_command(self, order_id: str, session: Optional[ClientSession] = None):
        return self.repository.unset_attribute(order_id, "current_command", session)

    def get_commands(self, order_id: str, session: Optional[ClientSession] = None) -> list[Command]:
        result = self.repository.get_attribute(order_id, "commands", session)
        return self.parse(result, list[Command])

    def add_command(self, order_id: str, command: Command, session: Optional[ClientSession] = None):
        return self.repository.push_to_list_attribute(order_id, "commands", self.encoder(command), session)

    def get_receipt(self, order_id: str, session: Optional[ClientSession] = None) -> list[ReceiptElement]:
        result = self.repository.get_attribute(order_id, "receipt", session)
        return self.parse(result, list[ReceiptElement])

    def set_receipt(self, order_id: str, receipt: list[ReceiptElement], session: Optional[ClientSession] = None):
        return self.repository.set_attribute(order_id, "receipt", self.encoder(receipt))
