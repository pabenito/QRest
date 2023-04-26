from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi import APIRouter, status, HTTPException
from app.database import db
from app.entities.models import Section, Element
from app.utils import json_lower_encoder

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

# Collections
menu = db["menu"]

@router.get("/", response_class=HTMLResponse)
def get(request: Request):
    return templates.TemplateResponse("menu.j2", {"request": request})

