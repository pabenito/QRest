from typing import Optional

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app import config
from app.api.frontend.services.receipt import ReceiptFrontend
from app.api.frontend.services.to_be_paid import ToBePaidFrontend

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

to_be_paid_frontend = ToBePaidFrontend()


@router.get("/mesa/{id}/por_pagar")
def get(request: Request, id: str, cliente: Optional[str] = None, error: Optional[str] = None, message: Optional[str] = None):
    if cliente:
        return RedirectResponse(f"http://{config.url}/mesa/{id}/por_pagar/total?cliente={cliente}")
    return RedirectResponse(f"http://{config.url}/mesa/{id}/por_pagar/total")


@router.get("/mesa/{id}/por_pagar/total")
def get_total(request: Request, id: str, cliente: Optional[str] = None, error: Optional[str] = None, message: Optional[str] = None):
    elements = to_be_paid_frontend.encode(to_be_paid_frontend.get_to_be_paid(id))
    if not elements:
        return RedirectResponse(f"http://{config.url}/mesa/{id}/carta?error=Error: Todavía no se ha confirmado ninguna comanda.")
    return templates.TemplateResponse("por_pagar.html.j2", {
        "request": request,
        "order_id": id,
        "client": cliente,
        "elements": elements,
        "error": error,
        "message": message})

@router.get("/mesa/{id}/por_pagar/individual")
def get_client(request: Request, id: str, cliente: Optional[str] = None, error: Optional[str] = None, message: Optional[str] = None):
    elements = to_be_paid_frontend.encode(to_be_paid_frontend.get_to_be_paid(id, cliente))
    if not elements:
        return RedirectResponse(f"http://{config.url}/mesa/{id}/carta?error=Error: Todavía no se ha confirmado ninguna comanda.")
    return templates.TemplateResponse("por_pagar.html.j2", {
        "request": request,
        "order_id": id,
        "client": cliente,
        "elements": elements,
        "error": error,
        "message": message,
        "individual": True})
