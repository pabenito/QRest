from fastapi import APIRouter, status

from app.core.entities.order import Request, Order, RequestPost
from app.core.use_cases.orders.current_requests import CurrentRequestsUseCases
from app.db.repositories.mongo_repositories.orders.current_requests import MongoCurrentRequestsRepository

# Create router
router = APIRouter()

use_cases = CurrentRequestsUseCases(repository=MongoCurrentRequestsRepository())


@router.post("/{id}",
             status_code=status.HTTP_201_CREATED,
             response_model=Request,
             response_model_exclude_unset=True,
             response_model_exclude_defaults=True)
def post_request(request: RequestPost):
    return use_cases.add(request)


@router.get("/{id}/requests",
            response_model=list[Request],
            response_model_exclude_unset=True,
            response_model_exclude_defaults=True)
def get_all_requests(order_id: str):
    return use_cases.get_all(order_id)
