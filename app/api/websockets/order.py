from pprint import pprint

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
from starlette.templating import Jinja2Templates

from app.api.frontend.entities.order import ExtendedElement
from app.core.entities.order import Element
from app.api.websockets.connection_manager import ConnectionManager
from app.core.use_cases.command import CommandUseCases
from app.db.repositories.mongo_repositories.command import MongoCommandRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.lib.utils import json_lower_encoder, parse_object

router = APIRouter()

manager = ConnectionManager()
templates = Jinja2Templates(directory="templates")
use_cases = CommandUseCases(order_repository=MongoOrderRepository(), command_repository=MongoCommandRepository())
encoder = json_lower_encoder
parser = parse_object


@router.websocket("/ws/mesa/{id}/cliente/{client}")
async def websocket_endpoint(websocket: WebSocket, id: str, client: str):
    await manager.connect(websocket, id)
    try:
        while True:
            data = await websocket.receive_json()
            pprint(data)
            element = parser(data, ExtendedElement)
            updated_element = use_cases.update_element(id, element)
            print("Element updated correctly:")
            pprint(updated_element)
            await manager.send_group(encoder(updated_element), id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, id)