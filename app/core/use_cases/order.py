from typing import Optional

from app.core.entities.order import OrderPost
from app.db.repositories.interfaces.order import IOrderRepository


class OrderUseCases:
    def __init__(self, repository: IOrderRepository):
        self.repository = repository

    def create(self, order: Optional[OrderPost] = None) -> str:
        if order is None:
            return self.repository.create(OrderPost())
        return self.repository.create(order)

    def delete(self, order: str):
        return self.repository.delete(order)

    def get_all(self):
        return self.repository.get_all()






