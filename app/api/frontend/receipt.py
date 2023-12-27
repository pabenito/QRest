from typing import Optional

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app import config
from app.api.frontend.services.receipt import ReceiptFrontend

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

receipt_frontend = ReceiptFrontend()


@router.get("/mesa/{id}/recibo")
def get(request: Request, id: str, error: Optional[str] = None, message: Optional[str] = None):
    elements = receipt_frontend.encode(receipt_frontend.get_receipt(id))
    if not elements:
        return RedirectResponse(f"http://{config.url}/mesa/{id}/carta?error=Error: Todavía no se ha confirmado ninguna comanda.")
    return templates.TemplateResponse("recibo.html.j2", {
        "request": request,
        "elements": elements,
        "error": error,
        "message": message})
