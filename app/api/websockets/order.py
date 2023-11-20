from fastapi import FastAPI, WebSocket, WebSocketDisconnect, WebSocketException, Request, status
from pydantic import TypeAdapter
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.core.entities.order import Element
from app.api.websockets import ConnectionManager
from app.core.use_cases.command import CommandUseCases
from app.db.repositories.mongo_repositories.command import MongoCommandRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.lib.utils import json_lower_encoder, parse_object

app = FastAPI()

manager = ConnectionManager()
templates = Jinja2Templates(directory="templates")
use_cases = CommandUseCases(order_repository=MongoOrderRepository(), command_repository=MongoCommandRepository())
encoder = json_lower_encoder
parser = parse_object

@app.get("/mesa/{group}/cliente/{client}", response_class=HTMLResponse)
async def get(request: Request, group: str, client: str):
    return templates.TemplateResponse("chat.html.j2", {
        "request": request,
        "group": group,
        "client": client})


@app.websocket("/ws/mesa/{group}/cliente/{client}")
async def websocket_endpoint(websocket: WebSocket, group: str, client: str):
    await manager.connect(websocket, group)
    try:
        while True:
            data = await websocket.receive_json()
            element = parser(data, Element)
            updated_element = use_cases.update_element(group, element)
            await manager.send_group(encoder(updated_element), group)
    except WebSocketDisconnect:
        manager.disconnect(websocket, group)