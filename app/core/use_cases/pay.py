from app.core.entities.order import ReceiptElement
from app.core.use_cases.services.pay import PayServices
from app.core.use_cases.services.receipt import ReceiptServices
from app.db.exceptions import PersistenceExceptionFactory
from app.db.repositories.interfaces.menu import IMenuRepository
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoTransactionManager


class PayUseCases:
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository
        self.transaction_manager = MongoTransactionManager
        self.persistence_exception_factory = PersistenceExceptionFactory("order")
        self.services = PayServices()

    def pay(self, order_id: str, elements: list[ReceiptElement]) -> list[ReceiptElement]:
        with self.transaction_manager() as session:
            to_be_paid = self.order_repository.get_to_be_paid(order_id, session)
            updated_to_be_paid = self.services.get_to_be_paid_after_payment(to_be_paid, elements)
            self.order_repository.set_to_be_paid(order_id, updated_to_be_paid, session)
            inserted_to_be_paid = self.order_repository.get_to_be_paid(order_id, session)
            return inserted_to_be_paid

    def pay_from_waiting_for_payment(self, order_id: str, elements: list[ReceiptElement]) -> list[list[ReceiptElement]]:
        with self.transaction_manager() as session:
            waiting_for_payment = self.order_repository.get_waiting_for_payment(order_id, session)

