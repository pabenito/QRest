from pydantic import BaseModel, HttpUrl


class ComplexModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True  # In order to allow ObjectId


# Carta

class Variant(ComplexModel):
    description: str
    image: HttpUrl | None
    price: float | None


class Variants(ComplexModel):
    name: str
    variants: list[Variant]


class Extra(BaseModel):
    description: str
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


# Allergens

class Allergen(BaseModel):
    name: str
    icon: HttpUrl
