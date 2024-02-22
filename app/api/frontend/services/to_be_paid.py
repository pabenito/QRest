from typing import Any, Optional

from app.entities.order import ReceiptElement
from app.use_cases.to_be_paid import ToBePaidUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.extra.utils import json_lower_encoder


class ToBePaidFrontend:
    def __init__(self):
        self.to_be_paid_use_cases = ToBePaidUseCases(order_repository=MongoOrderRepository())
        self.encoder = json_lower_encoder

    @staticmethod
    def encode(object: Any) -> dict:
        return json_lower_encoder(object)

    def get_to_be_paid(self, order_id: str, client: Optional[str] = None) -> list[ReceiptElement]:
        return self.to_be_paid_use_cases.get(order_id, client)

