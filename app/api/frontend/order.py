from pprint import pprint
from typing import Optional

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app.api.frontend.services.order import OrderFrontend
from app import config

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

order_frontend = OrderFrontend()


@router.get("/mesa/{id}/pedido")
def get(request: Request, id: str, error: Optional[str] = None, message: Optional[str] = None):
    elements = order_frontend.encode(order_frontend.get_current_command_with_extended_elements(id))
    if not elements:
        return RedirectResponse(f"http://{config.url}/mesa/{id}/carta?error=Error: No se han seleccionado elementos.")
    return templates.TemplateResponse("pedido.html.j2", {
        "request": request,
        "url": config.url,
        "ws_path": "/ws/comanda",
        "elements": elements,
        "order_id": id,
        "error": error,
        "message": message})
