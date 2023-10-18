from fastapi import APIRouter

from . import order, requests

router = APIRouter()

router.include_router(order.router)
router.include_router(requests.router)