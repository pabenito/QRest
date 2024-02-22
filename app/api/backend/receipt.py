from typing import Optional

from fastapi import APIRouter, status

from app.entities.order import ReceiptElement
from app.use_cases.receipt import ReceiptUseCases
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = ReceiptUseCases(order_repository=MongoOrderRepository(), menu_repository=MongoMenuRepository())


@router.post("/{id}/recibo", response_model=list[ReceiptElement], response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
def generate_receipt(id: str) -> list[ReceiptElement]:
    return use_cases.generate(id)

@router.get("/{id}/recibo", response_model=list[ReceiptElement], response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
def get_receipt(id: str, client: Optional[str] = None) -> list[ReceiptElement]:
    return use_cases.get(id, client)