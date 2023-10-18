from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.core.entities import Id


class Variant(BaseModel):
    name: str
    value: str


class Element(BaseModel):
    section: str
    element: str
    variants: Optional[list[Variant]] = None
    extras: Optional[list[str]] = None
    ingredients: Optional[list[str]] = None


class OrderElement(BaseModel):
    quantity: int
    element: Element


class Receipt(BaseModel):
    client: Optional[str] = None
    paid: Optional[datetime] = None
    total: float
    elements: OrderElement


class RequestPost(BaseModel):
    client: str
    order: str
    type: str
    element: Element


class Request(RequestPost):
    timestamp: datetime


class CommandPost(BaseModel):
    elements: list[OrderElement]


class Command(CommandPost):
    timestamp: datetime


class OrderPost(BaseModel):
    zone: Optional[str] = None
    table: Optional[str] = None


class OrderNew(OrderPost):
    created: datetime


class Order(OrderNew, Id):
    closed: Optional[datetime] = None
    current_requests: Optional[list[Request]] = None
    processed_requests: Optional[list[Request]] = None
    commands: Optional[list[Command]] = None
    total_receipt: Optional[Receipt] = None
    individual_receipts: Optional[list[Receipt]] = None
