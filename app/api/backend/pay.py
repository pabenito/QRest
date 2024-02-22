from fastapi import APIRouter, status

from app.entities.order import ReceiptElement
from app.use_cases.pay import PayUseCases
from app.db.repositories.mongo_repositories.order import MongoOrderRepository

router = APIRouter()
use_cases = PayUseCases(order_repository=MongoOrderRepository())


@router.post("/{id}/pagar", response_model=list[ReceiptElement], response_model_exclude_unset=True,
             status_code=status.HTTP_200_OK)
def pay(id: str, elements: list[ReceiptElement]) -> list[ReceiptElement]:
    return use_cases.pay(id, elements)


@router.post("/{id}/pagar/caja")
def waiting_for_payment(id: str, elements: list[ReceiptElement], websocket: str, client: str = None):
    return use_cases.wait_for_payment(id, elements, websocket, client)


@router.delete("/{id}/pagar/caja")
async def pay_from_waiting_for_payment(id: str, websocket_id: str):
    return await use_cases.pay_from_waiting_for_payment(id, websocket_id)
