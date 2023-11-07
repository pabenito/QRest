from dotenv import dotenv_values
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.testclient import TestClient

from app import app
from app.api.frontend.entities.order import ElementWithImage
from app.core.entities.menu import Section
from app.core.entities.order import Element
from app.lib.utils import pydantic_list_to_json

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

# API
api = TestClient(app)

# Config
config = dotenv_values("config.env")


@router.get("/", response_class=HTMLResponse)
def get(request: Request):
    return templates.TemplateResponse("menu.html.j2", {
        "request": request,
        "elements": pydantic_list_to_json(add_image_to_elements(sections, command))}


def add_image_to_elements(sections: list[Section], command: list[Element]) -> list[ElementWithImage]:
    image_dict = {}
    for section in sections:
        for element in section.elements:
            image_dict[(section.name, element.name)] = element.image

    elements_with_image = []
    for element in command:
        element_with_image = ElementWithImage(
            section=element.section,
            element=element.element,
            quantity=element.quantity,
            clients=element.clients,
            image=image_dict[(element.section, element.element)]
        )
        elements_with_image.append(element_with_image)
    return elements_with_image
