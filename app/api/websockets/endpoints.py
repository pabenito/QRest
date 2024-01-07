from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from starlette.templating import Jinja2Templates

from app.extra.exceptions import InvalidInputException
from app.api.services.extend_elment import extend_element
from app.extra.entities.order import Element
from app.core.command import CommandUseCases
from app.db.repositories.mongo_repositories.command import MongoCommandRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.extra.utils import json_lower_encoder, parse_object
from app.config import manager, wsdict

router = APIRouter()

templates = Jinja2Templates(directory="templates")
use_cases = CommandUseCases(order_repository=MongoOrderRepository(), command_repository=MongoCommandRepository())
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
                updated_element = use_cases.update_element(mesa, element)
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
async def websocket_endpoint(websocket: WebSocket, websocket_id: str):
    wsdict.add(websocket_id, websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        wsdict.remove(websocket_id)
    except Exception as error:
        wsdict.send(websocket_id, {"type": "error", "message": str(error)})
        wsdict.remove(websocket_id)
