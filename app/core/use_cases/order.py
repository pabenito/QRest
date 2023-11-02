from pydantic import TypeAdapter
from datetime import datetime

from app.core.entities.order import OrderPost, Order
from app.db.repositories.interfaces.order import IOrderRepository


class OrderUseCases:
    def __init__(self, repository: IOrderRepository):
        self.repository = repository

    def create(self, order: OrderPost) -> str:
        return self.repository.create(order)

    def delete(self, order: str) -> Order:
        return self.repository.delete(order)





