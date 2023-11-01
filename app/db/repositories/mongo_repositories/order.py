from app.core.entities.order import OrderPost, Element, Command, ReceiptElement
from app.core.exceptions.orders import OrderNotFoundException
from app.core.exceptions.orders import OrderOperationFailedException
from app.db.entities.order import VersionedOrder
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoRepository


class MongoOrder(MongoRepository):
    def __init__(self):
        super().__init__("order")

    def _exception_not_found(self, order_id: str) -> OrderNotFoundException:
        return OrderNotFoundException(order_id)

    def _exception_operation_failed(self, message: str) -> OrderOperationFailedException:
        return OrderOperationFailedException(message)


class MongoOrderRepository(IOrderRepository):
    def __init__(self):
        self.repository = MongoOrder()

    def create(self, order: OrderPost) -> str:
        new_order = VersionedOrder(**order.model_dump())
        return self.repository.insert_one(new_order.model_dump())

    def delete(self, order_id: str):
        self.repository.delete_one(order_id)

    def get_version(self, order_id: str) -> int:
        return self.repository.get_attribute(order_id, "version")

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
