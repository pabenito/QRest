from fastapi import APIRouter
from . import menu, command

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/carta"
)

router.include_router(
    command.router,
    prefix="/mesa",
    tags=["orders"]
)