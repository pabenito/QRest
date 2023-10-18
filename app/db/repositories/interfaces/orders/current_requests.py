from app.core.entities.order import Request


class ICurrentRequestsRepository:
    def add(self, order_id: str, request: Request) -> Request:
        pass

    def get_all(self, order_id: str) -> list[Request]:
        pass

    def remove_all(self, order_id: str) -> list[Request]:
        pass
