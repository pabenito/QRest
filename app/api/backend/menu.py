from fastapi import APIRouter

from app.core.entities.menu import Section
from app.core.use_cases.menu import MenuUseCases
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository

router = APIRouter()
use_cases = MenuUseCases(repository=MongoMenuRepository())


@router.get("/", response_model=list[Section], response_model_exclude_unset=True)
def get_menu():
    return use_cases.get_menu()
