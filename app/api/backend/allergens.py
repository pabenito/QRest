from fastapi import APIRouter

from app.use_cases.allergens import AllergensUseCases
from app.db.repositories.mongo_repositories.allergens import MongoAllergensRepository

router = APIRouter()
use_cases = AllergensUseCases(MongoAllergensRepository())


@router.get("/", response_model=dict)
def get() -> dict:
    return use_cases.get_allergens_dict()
