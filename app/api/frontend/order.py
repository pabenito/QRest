from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.frontend.services.order import OrderFrontend
from app import config

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

order_frontend = OrderFrontend()


@router.get("/", response_class=HTMLResponse)
def get(request: Request, mesa: str, client: str):
    elements = order_frontend.encode(order_frontend.get_current_command_with_extended_elements(mesa))
    return templates.TemplateResponse("pedido.html.j2", {
        "request": request,
        "url": config.url,
        "ws_path": "/ws/comanda",
        "elements": elements,
        "order_id": mesa,
        "client": client})
