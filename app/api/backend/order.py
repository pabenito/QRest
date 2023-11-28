from fastapi import APIRouter, status

from app.core.entities.order import OrderPost
from app.core.use_cases.order import OrderUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = OrderUseCases(MongoOrderRepository())


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(order: OrderPost) -> str:
    return use_cases.create(order)


@router.delete("/")
def delete(mesa: str):
    use_cases.delete(mesa)
