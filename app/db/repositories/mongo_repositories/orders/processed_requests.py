from bson import ObjectId

from app.core.entities.order import Request
from app.core.exceptions.orders import OrderOperationFailedException
from app.db import db
from app.db.repositories.interfaces.orders.processed_requests import IProcessedRequestsRepository
from app.lib.utils import json_lower_encoder
from .orders import MongoOrderRepository


class MongoProcessedRequestsRepository(IProcessedRequestsRepository):
    def __init__(self):
        self.db = db["orders"]
        self.json_encoder = json_lower_encoder
        self.order_repository = MongoOrderRepository()

    def add_all(self, order_id: str, requests: list[Request]) -> list[Request]:
        result = self.db.find_one_and_update(
            {"_id": ObjectId(order_id)},
            {"$set": {"processed_requests": self.json_encoder(requests)}})
        if result is None:
            raise OrderOperationFailedException(
                f"Add all requests to processed_requests in order with id {order_id} failed")
        return requests

    def get_all(self, order_id: str) -> list[Request]:
        order = self.order_repository.get_with_filter(order_id, {"current_requests": True})
        return order["current_requests"]
