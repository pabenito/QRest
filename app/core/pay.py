from typing import Optional

from app.extra.entities.order import ReceiptElement, WaitingForPayment
from app.core.services.pay import PayServices
from app.db.exceptions import PersistenceExceptionFactory
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoTransactionManager
from app.config import wsdict as websocket_manager


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

    def wait_for_payment(self, order_id: str, elements: list[ReceiptElement], websocket: str, client: Optional[str] = None):
        with self.transaction_manager() as session:
            if not self.order_repository.has_waiting_for_payment(order_id, session):
                self.order_repository.set_waiting_for_payment(order_id, [], session)
            waiting_for_payment = WaitingForPayment(websocket=websocket, client=client, elements=elements)
            self.order_repository.push_waiting_for_payment(order_id, waiting_for_payment, session)
            return waiting_for_payment

    def pay_from_waiting_for_payment(self, order_id: str, websocket: str):
        with self.transaction_manager() as session:
            if not self.order_repository.has_waiting_for_payment_in_list(order_id, WaitingForPayment(websocket=websocket), session):
                raise self.persistence_exception_factory.operation_failed(websocket, "waiting_for_payment")
            waiting_for_payment = self.order_repository.pull_waiting_for_payment(order_id, WaitingForPayment(websocket=websocket), session)
            self.pay(order_id, waiting_for_payment.elements)
            websocket_manager.send(websocket, {"type": "paid", "elements": waiting_for_payment.elements})
