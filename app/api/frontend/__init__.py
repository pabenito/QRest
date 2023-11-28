from fastapi import APIRouter

from app.api.frontend import menu
from app.api.frontend import order

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/carta"
)
router.include_router(
    order.router,
    prefix="/comanda"
)