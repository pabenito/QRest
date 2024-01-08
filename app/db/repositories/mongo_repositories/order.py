from typing import Optional
from pymongo.client_session import ClientSession

from app.extra.entities.order import OrderPost, Element, Command, ReceiptElement, Order, WaitingForPayment
from app.db.exceptions import FieldNotFoundException
from app.db.repositories.interfaces import IStandardRepository
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.extra.utils import parse_object, json_lower_encoder


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
        try:
            result = self.repository.get_attribute(order_id, "current_command", session)
        except FieldNotFoundException:
            return []
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
        return self.repository.set_attribute(order_id, "receipt", self.encoder(receipt), session)

    def set_to_be_paid(self, order_id: str, receipt: list[ReceiptElement], session: Optional[ClientSession] = None):
        return self.repository.set_attribute(order_id, "to_be_paid", self.encoder(receipt), session)

    def get_to_be_paid(self, order_id: str, session: Optional[ClientSession] = None) -> list[ReceiptElement]:
        result = self.repository.get_attribute(order_id, "to_be_paid", session)
        return self.parse(result, list[ReceiptElement])

    def get_all(self, session: Optional[ClientSession] = None) -> list[Order]:
        return self.repository.get_all(session)

    def has_receipt(self, order_id: str, session: Optional[ClientSession] = None):
        return self.repository.has_attribute(order_id, "receipt", session)

    def has_waiting_for_payment(self, order_id: str, session: Optional[ClientSession] = None):
        return self.repository.has_attribute(order_id, "waiting_for_payment", session)

    def has_waiting_for_payment_in_list(self, order_id: str, waiting_for_payment: WaitingForPayment, session: Optional[ClientSession] = None):
        return self.repository.has_element_in_list_attribute(order_id, "waiting_for_payment", self.encoder(waiting_for_payment), session)

    def set_waiting_for_payment(self, order_id: str, elements: list[WaitingForPayment], session: Optional[ClientSession] = None):
        return self.repository.set_attribute(order_id, "waiting_for_payment", self.encoder(elements), session)

    def get_waiting_for_payment(self, order_id: str, session: Optional[ClientSession] = None) -> list[WaitingForPayment]:
        result = self.repository.get_attribute(order_id, "waiting_for_payment", session)
        return self.parse(result, list[WaitingForPayment])

    def push_waiting_for_payment(self, order_id: str, waiting_for_payment: WaitingForPayment, session: Optional[ClientSession] = None):
        return self.repository.push_to_list_attribute(order_id, "waiting_for_payment", self.encoder(waiting_for_payment), session)

    def pull_waiting_for_payment(self, order_id: str, waiting_for_payment: WaitingForPayment, session: Optional[ClientSession] = None) -> WaitingForPayment:
        result = self.repository.pull_from_list_attribute(order_id, "waiting_for_payment", self.encoder(waiting_for_payment), session)
        return result