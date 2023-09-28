from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel, HttpUrl


class ComplexModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

# Carta

class Variant(ComplexModel):
    name: str
    image: Optional[HttpUrl] = None
    price: Optional[float] = None


class Variants(ComplexModel):
    name: str
    variants: list[Variant]


class Extra(BaseModel):
    name: str
    price: Optional[float] = None


class Tag(ComplexModel):
    name: str
    icon: Optional[HttpUrl] = None


class Element(ComplexModel):
    name: str
    image: Optional[HttpUrl] = None
    description: Optional[str] = None
    price: Optional[float] = None
    manager: str
    visible: bool = True
    ingredients: Optional[list[str]] = None
    allergens: Optional[list[str]] = None
    variants: Optional[list[Variants]] = None
    extras: Optional[list[Extra]] = None
    tags: Optional[list[Tag]] = None


class Section(ComplexModel):
    name: str
    visible: bool = True
    parent: Optional[str] = None
    elements: Optional[list[Element]] = None


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
    variants: Optional[list[OrderVariant]] = None
    extras: Optional[list[str]] = None
    ingredients: Optional[list[str]] = None

class Receipt(ComplexModel):
    total: float
    elements: list[OrderElement]

class TotalReceipt(ComplexModel):
    paid: Optional[datetime] = None
    receipt: Receipt

class IndividualReceipt(ComplexModel):
    paid: Optional[datetime] = None
    client: str
    receipt: Receipt

class FinalReceipt(ComplexModel):
    total: TotalReceipt
    individual: Optional[list[IndividualReceipt]] = None

class Request(ComplexModel):
    timestamp: Optional[datetime] = None
    client: str
    order: str
    type: str
    section: str
    element: str
    price: float
    variants: Optional[list[OrderVariant]] = None
    extras: Optional[list[str]] = None
    ingredients: Optional[list[str]] = None

class Command(ComplexModel):
    timestamp: Optional[datetime] = None
    requests: list[Request]
    receipts: list[Receipt]

class Order(ComplexModel):
    zone: Optional[str] = None
    table: Optional[str] = None
    created: Optional[datetime] = None
    closed: Optional[datetime] = None
    requests: list[Request] = []
    commands: list[Command] = []
    receipt: Optional[FinalReceipt] = None


# Allergens

class Allergen(BaseModel):
    name: str
    icon: HttpUrl
