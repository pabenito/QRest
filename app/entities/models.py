from datetime import datetime

from pydantic import BaseModel, HttpUrl


class ComplexModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True  # In order to allow ObjectId

# Carta

class Variant(ComplexModel):
    name: str
    image: HttpUrl | None
    price: float | None


class Variants(ComplexModel):
    name: str
    variants: list[Variant]


class Extra(BaseModel):
    name: str
    price: float | None


class Tag(ComplexModel):
    name: str
    icon: HttpUrl | None


class Element(ComplexModel):
    name: str
    image: HttpUrl | None
    description: str | None
    price: float | None
    manager: str
    visible: bool = True
    ingredients: list[str] | None
    allergens: list[str] | None
    variants: list[Variants] | None
    extras: list[Extra] | None
    tags: list[Tag] | None


class Section(ComplexModel):
    name: str
    visible: bool = True
    parent: str | None
    elements: list[Element] | None


# Pedidos

class OrderVariant(BaseModel):
    name: str
    value: str

class OrderElement(ComplexModel):
    section: str
    element: str
    quantity: int
    price: float
    manager: str
    variants: list[OrderVariant] | None
    extras: list[str] | None
    ingredients: list[str] | None

class Receipt(ComplexModel):
    total: float
    elements: list[OrderElement]

class TotalReceipt(ComplexModel):
    paid: datetime | None
    receipt: Receipt

class IndividualReceipt(ComplexModel):
    paid: datetime | None
    client: str
    receipt: Receipt

class FinalReceipt(ComplexModel):
    total: TotalReceipt
    individual: list[IndividualReceipt] | None

class Request(ComplexModel):
    timestamp: datetime
    client: str
    order: str
    type: str
    section: str
    element: str
    price: float
    variants: list[OrderVariant] | None
    extras: list[str] | None
    ingredients: list[str] | None

class Command(ComplexModel):
    timestamp: datetime
    requests: list[Request]
    receipts: list[Receipt]

class Order(ComplexModel):
    zone: str
    table: str
    created: datetime
    closed: datetime | None
    requests: list[Request] | None
    commands: list[Command] | None
    receipt: FinalReceipt | None


# Allergens

class Allergen(BaseModel):
    name: str
    icon: HttpUrl
