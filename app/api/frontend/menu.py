from pprint import pprint

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.frontend.services.menu import MenuFrontend

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

menu_frontend = MenuFrontend()


@router.get("/mesa/{id}/cliente/{client}/carta", response_class=HTMLResponse)
def get(request: Request, id: str, client):
    print("Extended sections:\n")
    pprint(menu_frontend.encode(menu_frontend.get_extended_sections(id)))
    return templates.TemplateResponse("menu.html.j2", {
        "request": request,
        "sections": menu_frontend.encode(menu_frontend.get_extended_sections(id)),
        "allergens": menu_frontend.encode(menu_frontend.get_allergens_dict()),
        "order_id": id,
        "client": client})