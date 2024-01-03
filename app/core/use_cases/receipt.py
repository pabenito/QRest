from pprint import pprint
from typing import Optional

from app.core.entities.order import ReceiptElement
from app.core.use_cases.services.receipt import ReceiptServices
from app.db.exceptions import PersistenceExceptionFactory
from app.db.repositories.interfaces.menu import IMenuRepository
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoTransactionManager


class ReceiptUseCases:
    def __init__(self, order_repository: IOrderRepository, menu_repository: IMenuRepository):
        self.order_repository = order_repository
        self.menu_repository = menu_repository
        self.transaction_manager = MongoTransactionManager
        self.persistence_exception_factory = PersistenceExceptionFactory("order")
        self.services = ReceiptServices()

    def generate(self, order_id: str) -> list[ReceiptElement]:
        with self.transaction_manager() as session:
            commands = self.order_repository.get_commands(order_id, session)
            menu = self.menu_repository.get_all(session)
            receipt = self.services.generate_receipt_from_commands(menu, commands)
            self.order_repository.set_receipt(order_id, receipt, session)
            self.order_repository.set_to_be_paid(order_id, receipt, session)
            inserted_receipt = self.order_repository.get_receipt(order_id, session)
            return inserted_receipt

    def get(self, order_id: str, client: Optional[str] = None) -> list[ReceiptElement]:
        receipt = self.order_repository.get_receipt(order_id)
        if client:
            return self.services.get_receipt_for_client(receipt, client)
        return receipt
