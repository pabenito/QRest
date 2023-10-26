from fastapi import APIRouter, status, HTTPException

from app.core.entities.order import Element, Command
from app.core.use_cases.command import CommandUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.db.repositories.mongo_repositories.command import MongoCommandRepository

router = APIRouter()
use_cases = CommandUseCases(order_repository=MongoOrderRepository(), command_repository=MongoCommandRepository())


@router.get("/",
            response_model=list[Element],
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def get(order: str):
    return use_cases.get(order)


@router.post("/confirmar",
             response_model=Command,
             response_model_exclude_unset=True,
             response_model_by_alias=False)
def confirm(order: str):
    return use_cases.confirm(order)


@router.put("/elementos",
            response_model=Element,
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def update_element(order: str, element: Element):
    return use_cases.update_element(order, element)
