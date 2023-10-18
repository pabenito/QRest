from app.core.entities.order import Order, OrderNew


class IOrderRepository:
    def create(self, order: OrderNew) -> Order:
        pass

    def get_all(self) -> list[Order]:
        pass

    def delete(self, order_id: str) -> Order:
        pass

    def get(self, order_id: str) -> Order:
        pass
