from fastapi import APIRouter

from app.api.frontend import menu, order, receipt

router = APIRouter()

router.include_router(menu.router)
router.include_router(order.router)
router.include_router(receipt.router)