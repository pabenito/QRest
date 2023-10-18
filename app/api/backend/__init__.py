from fastapi import APIRouter
from . import menu, orders

router = APIRouter()

router.include_router(menu.router)

router.include_router(
    orders.router,
    prefix="/orders",
    tags=["orders"]
)