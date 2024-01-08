from fastapi import APIRouter

from app.api.frontend import menu, order, receipt, to_be_paid, pay

router = APIRouter()

router.include_router(menu.router)
router.include_router(order.router)
router.include_router(receipt.router)
router.include_router(to_be_paid.router)
router.include_router(pay.router)