from bson import ObjectId

from app.core.entities.order import Request
from app.core.exceptions.orders import OrderOperationFailedException
from app.db import db
from app.db.repositories.interfaces.orders.current_requests import ICurrentRequestsRepository
from app.lib.utils import json_lower_encoder
from .orders import MongoOrderRepository


class MongoCurrentRequestsRepository(ICurrentRequestsRepository):
    def __init__(self):
        self.db = db["orders"]
        self.json_encoder = json_lower_encoder
        self.order_repository = MongoOrderRepository()

    def add(self, order_id: str, request: Request) -> Request:
        self.db.find_one_and_update(
            {"_id": ObjectId(order_id)},
            {"$push": {"current_requests": json_lower_encoder(request)}})
        return request

    def get_all(self, order_id: str) -> list[Request]:
        order = self.order_repository.get_with_filter(order_id, {"current_requests": True})
        return order["current_requests"]

    def remove_all(self, order_id: str) -> list[Request]:
        requests = self.get_all(order_id)
        result = self.db.find_one_and_update(
            {"_id": ObjectId(order_id)},
            {"$set": {"current_requests": None}})
        if result is None:
            raise OrderOperationFailedException(
                f"Remove all current_requests in order with id {order_id} failed")
        return requests
