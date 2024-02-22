from fastapi import APIRouter, status

from app.entities.order import Order, OrderPost
from app.use_cases.order import OrderUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = OrderUseCases(MongoOrderRepository())


@router.get("/", response_model=list[Order], response_model_exclude_unset=True)
def get_all() -> list[Order]:
    return use_cases.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(order: OrderPost) -> str:
    return use_cases.create(order)


@router.delete("/{id}")
def delete(id: str):
    use_cases.delete(id)
