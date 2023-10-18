from app.core.entities.order import Request


class IProcessedRequestsRepository:
    def add_all(self, order_id: str, requests: list[Request]) -> list[Request]:
        pass

    def get_all(self, order_id: str) -> list[Request]:
        pass
