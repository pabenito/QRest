from datetime import datetime

from app.core.entities.order import Request, RequestPost
from app.db.repositories.interfaces.orders.current_requests import ICurrentRequestsRepository
from app.core.exceptions.orders import OrderInvalidInputException


class CurrentRequestsUseCases:
    def __init__(self, repository: ICurrentRequestsRepository):
        self.repository = repository

    def add(self, request_post: RequestPost) -> Request:
        if request_post.type != "add" and request_post.type != "remove":
            raise OrderInvalidInputException(
                f'Request type is expected to be "add" or "remove", but found "{request_post.type}"')
        request = Request(**request_post.model_dump(), timestamp=datetime.now())
        return self.repository.add(request.order, request)

    def get_all(self, order_id: str) -> list[Request]:
        return self.repository.get_all(order_id)

    def remove_all(self, order_id: str) -> list[Request]:
        return self.repository.remove_all(order_id)
