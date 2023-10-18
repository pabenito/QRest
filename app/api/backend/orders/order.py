from fastapi import APIRouter, status

from app.core.entities.order import OrderPost, Order
from app.core.use_cases.orders.orders import OrderUseCases
from app.db.repositories.mongo_repositories.orders.orders import MongoOrderRepository

# Create router
router = APIRouter()

use_cases = OrderUseCases(repository=MongoOrderRepository())


@router.post("/",
             status_code=status.HTTP_201_CREATED,
             response_model=Order,
             response_model_exclude_unset=True,
             response_model_by_alias=False)
def create_order(order: OrderPost):
    return use_cases.create(order)

@router.get("/",
            response_model=list[Order],
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def get_all_orders():
    return use_cases.get_all()


@router.get("/{id}",
            response_model=Order,
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def get_order(order_id: str):
    return use_cases.get(order_id)

@router.delete("/{id}",
               response_model=Order,
               response_model_exclude_unset=True,
               response_model_by_alias=False)
def delete_order(order_id: str):
    return use_cases.delete(order_id)
