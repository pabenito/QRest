from typing import Optional

from fastapi import APIRouter, status

from app.core.entities.order import ReceiptElement
from app.core.use_cases.to_be_paid import ToBePaidUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = ToBePaidUseCases(order_repository=MongoOrderRepository())


@router.post("/{id}/por_pagar", response_model=list[ReceiptElement], response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
def get_to_be_paid(id: str, client: Optional[str] = None) -> list[ReceiptElement]:
    return use_cases.get(id, client)