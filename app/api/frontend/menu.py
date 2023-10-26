from dotenv import dotenv_values
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.testclient import TestClient

from app.api.backend._menu.allergens import router as allergens_client
from app.api.backend._menu.menu import router as menu_client

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

# API
menu = TestClient(menu_client)
allergens = TestClient(allergens_client)

# Config
config = dotenv_values("config.env")


@router.get("/", response_class=HTMLResponse)
def get(request: Request):
    return templates.TemplateResponse("_menu.html.j2", {
        "request": request,
        "sections": menu.get("/").json(),
        "allergens": allergens.get("/dict").json()})