from fastapi import APIRouter

from . import order, requests, commands

router = APIRouter()

router.include_router(order.router)
router.include_router(requests.router)
router.include_router(commands.router)