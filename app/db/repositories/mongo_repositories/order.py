from typing import Type, Any, Tuple

from bson import ObjectId

from app.core.entities.order import Order, OrderPost, Element, Command, ReceiptElement
from app.core.exceptions.orders import OrderNotFoundException, OrderOperationFailedException
from app.db.entities.order import VersionedOrder
from app import db
from app.db.repositories.interfaces.order import IOrderRepository
from app.core.exceptions.orders import OrderNotFoundException


class MongoOrder:
    @staticmethod
    def _get_db():
        return db.get_collection("order")

    def insert_one(self, order) -> str:
        result = self._get_db().insert_one(order)
        return str(result.inserted_id)

    def delete_one(self, order_id: str):
        result = self._get_db().delete_one({"_id": ObjectId(order_id)})
        if result.deleted_count != 1:
            raise OrderNotFoundException(order_id)

    def get_attribute(self, order_id: str, attribute: str):
        result = self._get_db().find_one({"_id": ObjectId(order_id)}, {attribute: True})
        if result is None:
            raise OrderNotFoundException(order_id)
        return result[attribute]

    def set_attribute(self, order_id: str, attribute: str, value):
        result = self._get_db().update_one({"_id": ObjectId(order_id)}, {"$set": {attribute: value}})
        if result.matched_count <= 0:
            raise OrderNotFoundException(order_id)
        if result.modified_count <= 0:
            raise OrderOperationFailedException(
                f"Error setting attribute. Order with id {order_id} already has {attribute} value: {value}")

    def unset_attribute(self, order_id: str, attribute: str):
        result = self._get_db().update_one({"_id": ObjectId(order_id)}, {"$unset": {attribute: ""}})
        if result.matched_count <= 0:
            raise OrderNotFoundException(order_id)
        if result.modified_count <= 0:
            raise OrderOperationFailedException(
                f"Error unsetting attribute. Order with id {order_id} does not have '{attribute}' attribute")

    def push_attribute(self, order_id: str, attribute: str, value):
        result = self._get_db().update_one({"_id": ObjectId(order_id)}, {"$push": {attribute: value}})
        if result.matched_count <= 0:
            raise OrderNotFoundException(order_id)
        if result.modified_count <= 0:
            raise OrderOperationFailedException(
                f"Error pushing attribute. Order with id {order_id} attribute '{attribute}' with value: {value}")

    def pop_attribute(self, order_id: str, attribute: str, last=True):
        index = 1 if last else -1
        result = self._get_db().update_one({"_id": ObjectId(order_id)}, {"$pop": {attribute: index}})
        if result.matched_count <= 0:
            raise OrderNotFoundException(order_id)
        if result.modified_count <= 0:
            position = "last" if last else "first"
            raise OrderOperationFailedException(
                f"Error popping attribute. Order with id {order_id} attribute '{attribute}' popping {position}")


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
