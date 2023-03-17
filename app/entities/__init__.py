from fastapi import APIRouter
from . import carta

router = APIRouter()

router.include_router(
    carta.router,
    prefix="/carta",
    tags=["carta"]
)