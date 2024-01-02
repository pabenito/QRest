from typing import Any, Optional

from app.core.entities.order import ReceiptElement
from app.core.use_cases.receipt import ReceiptUseCases
from app.core.use_cases.to_be_paid import ToBePaidUseCases
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.lib.utils import json_lower_encoder


class ToBePaidFrontend:
    def __init__(self):
        self.to_be_paid_use_cases = ToBePaidUseCases(order_repository=MongoOrderRepository())
        self.encoder = json_lower_encoder

    @staticmethod
    def encode(object: Any) -> dict:
        return json_lower_encoder(object)

    def get_to_be_paid(self, order_id: str, client: Optional[str] = None) -> list[ReceiptElement]:
        return self.to_be_paid_use_cases.get(order_id, client)

