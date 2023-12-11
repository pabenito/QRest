from fastapi import APIRouter, status, HTTPException

from app.core.entities.order import Order, OrderPost
from app.core.use_cases.order import OrderUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = OrderUseCases(MongoOrderRepository())


@router.get("/", status_code=status.HTTP_201_CREATED)
def get_all() -> list[Order]:
    return use_cases.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(order: OrderPost) -> str:
    return use_cases.create(order)


@router.delete("/{id}")
def delete(id: str):
    use_cases.delete(id)
