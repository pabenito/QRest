from fastapi import APIRouter
from . import menu

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/carta",
    tags=["carta"]
)