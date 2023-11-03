from typing import Type, Any, Tuple, Optional

from pymongo.client_session import ClientSession

from app.core.entities.order import Order, OrderPost, Element, Command, ReceiptElement


class IOrderRepository:
    def create(self, order: OrderPost, session: Optional[ClientSession] = None) -> str:
        pass

    def delete(self, order_id: str, session: Optional[ClientSession] = None):
        pass

    def get_current_command(self, order_id: str, session: Optional[ClientSession] = None) -> list[Element]:
        pass

    def delete_current_command(self, order_id: str, session: Optional[ClientSession] = None):
        pass

    def get_commands(self, order_id: str, session: Optional[ClientSession] = None) -> list[Command]:
        pass

    def add_command(self, order_id: str, command: Command, session: Optional[ClientSession] = None):
        pass

    def get_receipt(self, order_id: str, session: Optional[ClientSession] = None) -> list[ReceiptElement]:
        pass

    def set_receipt(self, order_id: str, receipt: list[ReceiptElement], session: Optional[ClientSession] = None):
        pass
