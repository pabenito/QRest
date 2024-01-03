from pprint import pprint
from typing import Optional

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app import config
from app.api.frontend.services.menu import MenuFrontend
from app.api.frontend.services.order import OrderFrontend

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

menu_frontend = MenuFrontend()
order_frontend = OrderFrontend()


@router.get("/carta")
def redirect_new_order_carta():
    order_id = menu_frontend.create_order()
    return RedirectResponse(url=f"/mesa/{order_id}/carta")

@router.get("/mesa/{id}")
def get(request: Request, id: str):
    return RedirectResponse(url=f"/mesa/{id}/carta")

@router.get("/mesa/{id}/carta", response_class=HTMLResponse)
def get(request: Request, id: str, error: Optional[str] = None, message: Optional[str] = None):
    return templates.TemplateResponse("menu.html.j2", {
        "request": request,
        "url": config.url,
        "ws_path": "/ws/comanda",
        "sections": menu_frontend.encode(menu_frontend.get_extended_sections(id)),
        "allergens": menu_frontend.encode(menu_frontend.get_allergens_dict()),
        "order_id": id,
        "elements": order_frontend.get_current_command(id),
        "error": error,
        "message": message})
