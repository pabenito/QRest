from typing import Optional

from app.core.entities.order import ReceiptElement
from app.core.use_cases.services.to_be_paid import ToBePaidServices
from app.db.exceptions import PersistenceExceptionFactory
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoTransactionManager


class ToBePaidUseCases:
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository
        self.transaction_manager = MongoTransactionManager
        self.persistence_exception_factory = PersistenceExceptionFactory("order")
        self.services = ToBePaidServices()

    def get(self, order_id: str, client: Optional[str]) -> list[ReceiptElement]:
        try:
            to_be_paid = self.order_repository.get_to_be_paid(order_id)
            if client:
                return self.services.get_to_be_paid_for_client(to_be_paid, client)
            return to_be_paid
        except:
            return []
