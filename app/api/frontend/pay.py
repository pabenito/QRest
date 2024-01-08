from pprint import pprint
from typing import Optional

from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app import config
from app.api.frontend.services.pay import PayFrontend
from app.api.frontend.services.receipt import ReceiptFrontend

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

pay_frontend = PayFrontend()

@router.get("/mesa/{id}/caja")
def get(request: Request, id: str, error: Optional[str] = None, message: Optional[str] = None):
    try:
        waiting_list = pay_frontend.encode(pay_frontend.get_waiting_for_payment(id))
    except Exception:
        waiting_list = []
        error = "No hay ningún pago pendiente"
    pprint(waiting_list)
    return templates.TemplateResponse("pago.html.j2", {
        "request": request,
        "order_id": id,
        "waiting_list": waiting_list,
        "error": error,
        "message": message})
