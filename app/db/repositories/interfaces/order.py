from typing import Optional
from abc import ABC, abstractmethod
from pymongo.client_session import ClientSession

from app.extra.entities.order import OrderPost, Element, Command, ReceiptElement, Order, WaitingForPayment


class IOrderRepository(ABC):
    @abstractmethod
    def create(self, order: OrderPost, session: Optional[ClientSession] = None) -> str:
        pass

    @abstractmethod
    def delete(self, order_id: str, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def exists(self, order_id: str, session: Optional[ClientSession] = None) -> bool:
        pass

    @abstractmethod
    def has_current_command(self, order_id: str, session: Optional[ClientSession] = None) -> bool:
        pass

    @abstractmethod
    def get_current_command(self, order_id: str, session: Optional[ClientSession] = None) -> list[Element]:
        pass

    @abstractmethod
    def delete_current_command(self, order_id: str, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def get_commands(self, order_id: str, session: Optional[ClientSession] = None) -> list[Command]:
        pass

    @abstractmethod
    def add_command(self, order_id: str, command: Command, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def get_receipt(self, order_id: str, session: Optional[ClientSession] = None) -> list[ReceiptElement]:
        pass

    @abstractmethod
    def set_receipt(self, order_id: str, receipt: list[ReceiptElement], session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def get_to_be_paid(self, order_id: str, session: Optional[ClientSession] = None) -> list[ReceiptElement]:
        pass

    @abstractmethod
    def set_to_be_paid(self, order_id: str, receipt: list[ReceiptElement], session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def get_all(self, session: Optional[ClientSession] = None) -> list[Order]:
        pass

    @abstractmethod
    def has_receipt(self, order_id: str, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def has_waiting_for_payment(self, order_id: str, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def has_waiting_for_payment_in_list(self, order_id: str, waiting_for_payment: WaitingForPayment, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def set_waiting_for_payment(self, order_id: str, elements: list[WaitingForPayment], session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def get_waiting_for_payment(self, order_id: str, session: Optional[ClientSession] = None) -> list[WaitingForPayment]:
        pass

    @abstractmethod
    def push_waiting_for_payment(self, order_id: str, waiting_for_payment: WaitingForPayment, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def pull_waiting_for_payment(self, order_id: str, waiting_for_payment: WaitingForPayment, session: Optional[ClientSession] = None) -> WaitingForPayment:
        pass
