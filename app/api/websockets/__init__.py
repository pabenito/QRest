from fastapi import APIRouter

from app.api.websockets import endpoints

router = APIRouter()

router.include_router(endpoints.router)