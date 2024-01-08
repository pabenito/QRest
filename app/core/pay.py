from typing import Optional

from app.extra.entities.order import ReceiptElement, WaitingForPayment
from app.core.services.pay import PayServices
from app.db.exceptions import PersistenceExceptionFactory
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.mongo_repositories import MongoTransactionManager
from app.config import wsdict as websocket_manager
from app.extra.utils import json_lower_encoder


class PayUseCases:
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository
        self.transaction_manager = MongoTransactionManager
        self.persistence_exception_factory = PersistenceExceptionFactory("order")
        self.services = PayServices()

    def pay(self, order_id: str, elements: list[ReceiptElement]) -> list[ReceiptElement]:
        with self.transaction_manager() as session:
            self._pay(order_id, elements, session)

    def wait_for_payment(self, order_id: str, elements: list[ReceiptElement], websocket_id: str, client: Optional[str] = None):
        with self.transaction_manager() as session:
            if not self.order_repository.has_waiting_for_payment(order_id, session):
                self.order_repository.set_waiting_for_payment(order_id, [], session)
            waiting_for_payment = WaitingForPayment(websocket=websocket_id, client=client, elements=elements)
            self.order_repository.push_waiting_for_payment(order_id, waiting_for_payment, session)
            return waiting_for_payment

    async def pay_from_waiting_for_payment(self, order_id: str, websocket_id: str):
        with self.transaction_manager() as session:
            if not self.order_repository.has_waiting_for_payment_in_list(order_id, WaitingForPayment(websocket=websocket_id), session):
                raise self.persistence_exception_factory.operation_failed(websocket_id, "waiting_for_payment")
            self.order_repository.pull_waiting_for_payment(order_id, WaitingForPayment(websocket=websocket_id), session)
            waiting_for_payment_list = self.order_repository.get_waiting_for_payment(order_id)
            waiting_for_payment = None
            for waiting_for_payment_element in waiting_for_payment_list:
                if waiting_for_payment_element.websocket == websocket_id:
                    waiting_for_payment = waiting_for_payment_element
            if waiting_for_payment is None:
                raise Exception(f"Wait_for_payment with id {websocket_id} does not exists")
            self._pay(order_id, waiting_for_payment.elements, session)
            await websocket_manager.send(websocket_id, {"type": "paid", "elements": json_lower_encoder(waiting_for_payment.elements)})

    def _pay(self, order_id: str, elements: list[ReceiptElement], session) -> list[ReceiptElement]:
        to_be_paid = self.order_repository.get_to_be_paid(order_id, session)
        updated_to_be_paid = self.services.get_to_be_paid_after_payment(to_be_paid, elements)
        self.order_repository.set_to_be_paid(order_id, updated_to_be_paid, session)
        inserted_to_be_paid = self.order_repository.get_to_be_paid(order_id, session)
        return inserted_to_be_paid