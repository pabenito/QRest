from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.frontend.services.order import OrderFrontend

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

order_frontend = OrderFrontend()


@router.get("/mesa/{id}/pedido", response_class=HTMLResponse)
def get(request: Request, id: str):
    elements = order_frontend.encode(order_frontend.get_current_command_with_extended_elements(id))
    return templates.TemplateResponse("pedido.html.j2", {
        "request": request,
        "elements": elements,
        "order_id": id})
