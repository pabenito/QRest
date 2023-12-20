from fastapi import APIRouter
from . import menu, command, order, receipt

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/carta"
)

router.include_router(
    command.router,
    prefix="/mesa"
)

router.include_router(
    order.router,
    prefix="/mesa"
)

router.include_router(
    receipt.router,
    prefix="/mesa"
)