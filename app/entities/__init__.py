from fastapi import APIRouter
from . import menu, allergens, orders

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/carta",
    tags=["carta"]
)

router.include_router(
    allergens.router,
    prefix="/allergens",
    tags=["allergens"]
)

router.include_router(
    orders.router,
    prefix="/orders",
    tags=["orders"]
)