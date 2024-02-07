from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.extra.entities import Id


class Variant(BaseModel):
    name: str
    value: str


class BasicElement(BaseModel):
    section: str
    element: str
    variants: Optional[list[Variant]] = None
    extras: Optional[list[str]] = None
    ingredients: Optional[list[str]] = None


class Element(BasicElement):
    quantity: int
    clients: list[str]


class ReceiptElement(Element):
    price: float
    total: float


class Command(BaseModel):
    timestamp: datetime
    elements: list[Element]


class OrderPost(BaseModel):
    zone: Optional[str] = None
    table: Optional[str] = None

class OrderNew(OrderPost):
    date: datetime = Field(default_factory=datetime.now)


class WaitingForPayment(BaseModel):
    websocket: str
    client: Optional[str] = None
    elements: Optional[list[ReceiptElement]] = None


class Order(OrderNew, Id):
    current_command: Optional[list[Element]] = None
    commands: Optional[list[Command]] = None
    receipt: Optional[list[ReceiptElement]] = None
    to_be_paid: Optional[list[ReceiptElement]] = None
    waiting_for_payment: Optional[list[WaitingForPayment]] = None
    paid: Optional[bool] = None
