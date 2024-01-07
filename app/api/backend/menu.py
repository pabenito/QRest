from fastapi import APIRouter

from app.extra.entities.menu import Section
from app.core.menu import MenuUseCases
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository

router = APIRouter()
use_cases = MenuUseCases(repository=MongoMenuRepository())


@router.get("/", response_model=list[Section], response_model_exclude_unset=True)
def get_menu() -> list[Section]:
    return use_cases.get_menu()
