from fastapi import APIRouter

from app.api import backend
from app.api import frontend
from app.api import websockets

router = APIRouter()

router.include_router(
    backend.router,
    prefix="/backend"
)
router.include_router(frontend.router)
router.include_router(websockets.router)