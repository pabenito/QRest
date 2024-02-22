from typing import Any

from app.entities.order import ReceiptElement
from app.use_cases.pay import PayUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.extra.utils import json_lower_encoder


class PayFrontend:
    def __init__(self):
        self.pay_use_cases = PayUseCases(order_repository=MongoOrderRepository())
        self.encoder = json_lower_encoder

    @staticmethod
    def encode(object: Any) -> dict:
        return json_lower_encoder(object)

    def get_waiting_for_payment(self, order_id: str) -> list[ReceiptElement]:
        return self.pay_use_cases.get_waiting_for_payment(order_id)

