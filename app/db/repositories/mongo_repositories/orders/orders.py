import pymongo
from bson import ObjectId
from pydantic import ValidationError

from app.db import db
from app.core.exceptions.orders import *
from app.db.repositories.interfaces.orders.orders import IOrderRepository
from app.core.entities.order import Order, OrderNew
from app.lib.utils import json_lower_encoder


class MongoOrderRepository(IOrderRepository):
    def __init__(self):
        self.db = db["orders"]
        self.json_encoder = json_lower_encoder

    def create(self, order: OrderNew) -> Order:
        result = self.db.insert_one(self.json_encoder(order))
        created_order = self.db.find_one({"_id": result.inserted_id})
        return created_order

    def get(self, order_id: str) -> Order:
        order = self.db.find_one({"_id": ObjectId(order_id)})
        if order is None:
            raise OrderNotFoundException(order_id)
        try:
            validated_order = Order.model_validate(order)
        except ValidationError as e:
            raise OrderValidationException(str(e))
        return validated_order

    def get_with_filter(self, order_id: str, filter_query: dict) -> dict:
        order = self.db.find_one({"_id": ObjectId(order_id)}, filter_query)
        if order is None:
            raise OrderNotFoundException(order_id)
        return order

    def get_all(self) -> list[Order]:
        return list(self.db.find().sort("created", pymongo.DESCENDING))

    def delete(self, order_id: str) -> Order:
        order = self.get(order_id)
        result = self.db.delete_one({"_id": ObjectId(order_id)})
        if result.deleted_count != 1:
            raise OrderNotFoundException(order_id)
        return order

