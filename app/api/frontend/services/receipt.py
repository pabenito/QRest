from typing import Any, Optional

from app.entities.order import ReceiptElement
from app.use_cases.receipt import ReceiptUseCases
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.extra.utils import json_lower_encoder


class ReceiptFrontend:
    def __init__(self):
        self.receipt_use_cases = ReceiptUseCases(order_repository=MongoOrderRepository(), menu_repository=MongoMenuRepository())
        self.encoder = json_lower_encoder

    @staticmethod
    def encode(object: Any) -> dict:
        return json_lower_encoder(object)

    def get_receipt(self, order_id: str, client: Optional[str] = None) -> list[ReceiptElement]:
        return self.receipt_use_cases.get(order_id, client)