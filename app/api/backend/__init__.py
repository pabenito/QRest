from fastapi import APIRouter
from . import menu, command, order

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/carta"
)

router.include_router(
    command.router,
    prefix="/comanda"
)

router.include_router(
    order.router,
    prefix="/mesa"
)