from bson import ObjectId

from app.core.entities.order import Command
from app.db import db
from app.db.repositories.interfaces.orders.commands import ICommandRepository
from app.db.repositories.mongo_repositories.orders.orders import MongoOrderRepository
from app.lib.utils import json_lower_encoder


class MongoCommandRepository(ICommandRepository):
    def __init__(self):
        self.db = db["orders"]
        self.json_encoder = json_lower_encoder
        self.order_repository = MongoOrderRepository()

    def add(self, order_id: str, command: Command) -> Command:
        if self.order_repository.has_field(order_id, "commands"):
            self.db.find_one_and_update(
                {"_id": ObjectId(order_id)},
                {"$push": {"commands": json_lower_encoder(command)}})
        else:
            self.db.find_one_and_update(
                {"_id": ObjectId(order_id)},
                {"$set": {"commands": json_lower_encoder([command])}})
        return command

    def get_all(self, order_id: str) -> list[Command]:
        order = self.order_repository.get_with_filter(order_id, {"commands": True})
        return order["commands"]