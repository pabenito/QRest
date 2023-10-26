from fastapi import APIRouter
from . import menu, command

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/carta"
)

router.include_router(
    order.router,
    prefix="/mesa/{order}/pedido",
    tags=["orders"]
)