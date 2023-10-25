from fastapi import APIRouter, status, HTTPException

from app.core.entities.order import Order, Element

# Create router
router = APIRouter()


@router.get("mesa/{order}/pedido/",
            response_model=Order,
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def get_current_command(order: str):
    pass


@router.post("mesa/{order}/pedido/confirmar",
             response_model=Order,
             response_model_exclude_unset=True,
             response_model_by_alias=False)
def confirm_current_command(order: str):
    pass


@router.put("mesa/{order}/pedido/elementos",
            response_model=Element,
            response_model_exclude_unset=True,
            response_model_by_alias=False)
def confirm_current_command(order: str, element: Element):
    pass
