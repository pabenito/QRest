from fastapi import APIRouter

from app.extra.entities.menu import Element
from app.core.command import CommandUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.db.repositories.mongo_repositories.command import MongoCommandRepository

router = APIRouter()
use_cases = CommandUseCases(order_repository=MongoOrderRepository(), command_repository=MongoCommandRepository())


@router.get("/{id}/pedido",
            response_model=list[Element],
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def get(id: str) -> list[Element]:
    return use_cases.get(id)


@router.post("/{id}/pedido/confirmar",
             response_model_exclude_unset=True,
             response_model_by_alias=False)
def confirm(id: str):
    use_cases.confirm(id)


@router.put("/{id}/pedido/elementos",
            response_model=Element,
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def update_element(id: str, element: Element) -> Element:
    return use_cases.update_element(id, element)
