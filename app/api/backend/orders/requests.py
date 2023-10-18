from fastapi import APIRouter, status

from app.core.entities.order import Request, Order, RequestPost
from app.core.use_cases.orders.requests import RequestUseCases
from app.db.repositories.mongo_repositories.orders.current_requests import MongoCurrentRequestsRepository

# Create router
router = APIRouter()

use_cases = RequestUseCases(repository=MongoCurrentRequestsRepository())


@router.post("/{id}", status_code=status.HTTP_201_CREATED, response_model=Request, response_model_exclude_unset=True)
def post_request(order_id: str, request: RequestPost):
    return use_cases.add(request)


@router.get("/{id}/requests", response_model=list[Request], response_model_exclude_unset=True)
def get_all_requests(order_id: str):
    return use_cases.get_all(order_id)
