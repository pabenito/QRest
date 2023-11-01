from typing import Type, Any, Tuple, Optional

from app.core.entities.order import Order, OrderPost, Element, Command, ReceiptElement


class IOrderRepository:
    def create(self, order: OrderPost) -> str:
        pass

    def delete(self, order_id: str):
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
