from datetime import datetime

from app.core.entities.order import Order, OrderNew, OrderPost
from app.db.repositories.interfaces.orders.orders import IOrderRepository


class OrderUseCases:
    def __init__(self, repository: IOrderRepository):
        self.repository = repository

    def create(self, order_post: OrderPost) -> Order:
        order_new = OrderNew(**order_post.model_dump(), created=datetime.now())
        order = self.repository.create(order_new)
        return order

    def get(self, order_id: str) -> Order:
        return self.repository.get(order_id)

    def get_all(self) -> list[Order]:
        return self.repository.get_all()

    def delete(self, order_id: str) -> Order:
        return self.repository.delete(order_id)
