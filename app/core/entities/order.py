from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.core.entities import Id


class Variant(BaseModel):
    name: str
    value: str


class Element(BaseModel):
    version: Optional[int] = 0
    section: str
    element: str
    quantity: int
    clients: list[str]
    variants: Optional[list[Variant]] = None
    extras: Optional[list[str]] = None
    ingredients: Optional[list[str]] = None


class ReceiptElement(Element):
    price: float


class Command(BaseModel):
    timestamp: datetime
    elements: list[Element]


class OrderPost(BaseModel):
    zone: Optional[str] = None
    table: Optional[str] = None


class OrderNew(OrderPost):
    date: datetime = Field(default_factory=datetime.now)
    version: int = 0


class Order(OrderNew, Id):
    current_command: Optional[list[Element]] = None
    commands: Optional[list[Command]] = None
    receipt: Optional[list[ReceiptElement]] = None
    to_be_paid: Optional[list[ReceiptElement]] = None
    paid: Optional[bool] = None
