from fastapi import APIRouter, status, HTTPException

from app.core.entities.order import Order, Element
from app.core.use_cases.orders.orders import OrderUseCases
from app.db.repositories.mongo_repositories.orders.orders import MongoOrderRepository

router = APIRouter()
use_cases = OrderUseCases(repository=MongoOrderRepository())

@router.get("/",
            response_model=Order,
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def get_current_command(order: str):
    pass


@router.post("/confirmar",
             response_model=Order,
             response_model_exclude_unset=True,
             response_model_by_alias=False)
def confirm_current_command(order: str):
    pass


@router.put("/elementos",
            response_model=Element,
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def confirm_current_command(order: str, element: Element):
    pass
