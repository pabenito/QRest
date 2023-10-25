from fastapi import APIRouter
from . import menu, order

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/empleados",
)

router.include_router(
    orders.router,
    prefix="/orders",
    tags=["orders"]
)