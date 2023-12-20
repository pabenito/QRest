from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.frontend.services.receipt import ReceiptFrontend

# Create router
router = APIRouter()

# Load templates directory
templates = Jinja2Templates(directory="templates")

receipt_frontend = ReceiptFrontend()


@router.get("/mesa/{id}/recibo", response_class=HTMLResponse)
def get(request: Request, id: str):
    elements = receipt_frontend.encode(receipt_frontend.get_receipt(id))
    return templates.TemplateResponse("recibo.html.j2", {
        "request": request,
        "elements": elements})
