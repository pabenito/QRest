from fastapi import APIRouter, status

from app.core.entities.order import ReceiptElement
from app.core.use_cases.receipt import ReceiptUseCases
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = ReceiptUseCases(order_repository=MongoOrderRepository(), menu_repository=MongoMenuRepository())


@router.post("/{id}/recibo", response_model=list[ReceiptElement], response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
def generate_receipt(id: str) -> list[ReceiptElement]:
    return use_cases.generate(id)