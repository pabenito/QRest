from app.core.entities.order import Request
from app.db.repositories.interfaces.orders.processed_requests import IProcessedRequestsRepository


class ProcessedRequestsUseCases:
    def __init__(self, repository: IProcessedRequestsRepository):
        self.repository = repository

    def add_all(self, order_id: str, requests: list[Request]) -> list[Request]:
        self.repository.add_all(order_id, requests)

    def get_all(self, order_id: str) -> list[Request]:
        self.repository.get_all(order_id)