from fastapi import APIRouter

from . import menu, allergens

router = APIRouter()

router.include_router(
    menu.router,
    prefix="/menu",
    tags=["menu"]
)

router.include_router(
    allergens.router,
    prefix="/allergens",
    tags=["allergens"]
)