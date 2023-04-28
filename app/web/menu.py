import pprint

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi import APIRouter, status, HTTPException
from app.database import db
from app.entities.models import Section, Element
from app.utils import json_lower_encoder

from fastapi.testclient import TestClient
from app.entities.menu import router as menu_client
from app.entities.allergens import router as allergens_client

from dotenv import dotenv_values

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

# API
menu = TestClient(menu_client)
allergens = TestClient(allergens_client)

# Config
config = dotenv_values("config.env")


@router.get("/")
def get():
    return RedirectResponse(f"/{config['MAIN_SECTION']}")


@router.get("/{section}", response_class=HTMLResponse)
def get(request: Request, section: str):
    pprint.pprint(menu.get(f"/{section}"))
    return templates.TemplateResponse("menu.html.j2", {
        "request": request,
        "sections": menu.get("/sections").json(),
        "section": menu.get(f"/{section}", params={"ids": True}).json(),
        "allergens": allergens.get("/dict").json()})
