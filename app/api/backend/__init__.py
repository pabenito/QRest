from fastapi import APIRouter
from . import menu, command, order, receipt, to_be_paid, pay, to_be_paid

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

router.include_router(
    pay.router,
    prefix="/mesa"
)

router.include_router(
    to_be_paid.router,
    prefix="/mesa"
)