from fastapi import APIRouter

from app.api.websockets import order

router = APIRouter()

router.include_router(order.router)