from pprint import pprint
from time import sleep
from typing import Optional

from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from starlette.templating import Jinja2Templates

from app.core.pay import PayUseCases
from app.extra.exceptions import InvalidInputException
from app.api.services.extend_elment import extend_element
from app.extra.entities.order import Element, ReceiptElement
from app.core.command import CommandUseCases
from app.db.repositories.mongo_repositories.command import MongoCommandRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.extra.utils import json_lower_encoder, parse_object
from app.config import manager, wsdict

router = APIRouter()

templates = Jinja2Templates(directory="templates")
command_use_cases = CommandUseCases(order_repository=MongoOrderRepository(), command_repository=MongoCommandRepository())
pay_use_cases = PayUseCases(order_repository=MongoOrderRepository())
encoder = json_lower_encoder
parser = parse_object


@router.websocket("/ws/comanda")
async def websocket_endpoint(websocket: WebSocket, mesa: str):
    await manager.connect(websocket, mesa)
    try:
        while True:
            data = await websocket.receive_json()
            element = parser(data, Element)
            try:
                updated_element = command_use_cases.update_element(mesa, element)
                extended_element = extend_element(updated_element)
                await manager.send_group(encoder(extended_element), mesa)
            except InvalidInputException as error:
                await manager.send_single(websocket, {"type": "error", "message": str(error)})
    except WebSocketDisconnect:
        manager.disconnect(websocket, mesa)
    except Exception as error:
        await manager.send_single(websocket, {"type": "error", "message": str(error)})
        manager.disconnect(websocket, mesa)


@router.websocket("/ws/pay")
async def websocket_endpoint(websocket: WebSocket, mesa: str, websocket_id: str, client_id: Optional[str] = None):
    await wsdict.add(websocket_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            wait_for_payment = parser(data, list[ReceiptElement])
            pay_use_cases.wait_for_payment(mesa, wait_for_payment, websocket_id, client_id)
            #sleep(5);
            await pay_use_cases.pay_from_waiting_for_payment(mesa, websocket_id)
    except WebSocketDisconnect:
        wsdict.remove(websocket_id)
    except Exception as error:
        await wsdict.send(websocket_id, {"type": "error", "message": str(error)})
        wsdict.remove(websocket_id)