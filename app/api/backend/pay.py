from fastapi import APIRouter, status

from app.core.entities.order import ReceiptElement
from app.core.use_cases.pay import PayUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = PayUseCases(order_repository=MongoOrderRepository())


@router.post("/{id}/pagar", response_model=list[ReceiptElement], response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
def pay(id: str, elements: list[ReceiptElement]) -> list[ReceiptElement]:
    return use_cases.pay(id, elements)