from fastapi import APIRouter, status, HTTPException

from app.core.entities.order import Order, OrderPost
from app.core.use_cases.order import OrderUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = OrderUseCases(MongoOrderRepository())


@router.post("/")
def create(order: OrderPost) -> str:
    return use_cases.create(order)


@router.delete("/{order_id}")
def delete(order_id: str) -> Order:
    return use_cases.delete(order_id)
