from typing import Dict

from fastapi.websockets import WebSocket


class WebSocketManagerDict:
    def __init__(self):
        self.websockets: dict[str, WebSocket] = {}

    async def add(self, websocket_id: str, websocket: WebSocket):
        await websocket.accept()
        self.websockets[websocket_id] = websocket

    def remove(self, websocket_id: str):
        del self.websockets[websocket_id]

    async def send(self, websocket_id: str, message):
        await self.websockets[websocket_id].send_json(message)


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, list[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, group: str):
        await websocket.accept()
        if not group in self.active_connections:
            self.active_connections[group] = []
        self.active_connections[group].append(websocket)

    def disconnect(self, websocket: WebSocket, group: str):
        self.active_connections[group].remove(websocket)

    async def send_single(self, websocket: WebSocket, message):
        await websocket.send_json(message)


    async def send_group(self, message, group: str):
        for connection in self.active_connections[group]:
            await connection.send_json(message)