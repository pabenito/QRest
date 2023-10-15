from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.models.common import ComplexModel, Id


class Variant(BaseModel):
    name: str
    value: str


class Element(BaseModel):
    section: str
    element: str
    price: float
    manager: str
    variants: Optional[list[Variant]] = None
    extras: Optional[list[str]] = None
    ingredients: Optional[list[str]] = None


class OrderElement(ComplexModel):
    quantity: int
    element: Element


class Receipt(ComplexModel):
    client: Optional[str] = None
    paid: Optional[datetime] = None
    total: float
    elements: list[OrderElement] = None


class Request(ComplexModel):
    id: Optional[str] = None
    timestamp: Optional[datetime] = None
    client: str
    order: str
    type: str
    element: Element


class Command(ComplexModel):
    timestamp: datetime
    elements: list[OrderElement] = None


class Order(ComplexModel):
    zone: Optional[str] = None
    table: Optional[str] = None
    created: Optional[datetime] = None
    closed: Optional[datetime] = None
    requests: list[Request] = []
    commands: list[Command] = []
    total_receipt: Optional[Receipt] = None
    individual_receipts: Optional[list[Receipt]] = None


class OrderId(Order, Id):
    pass
