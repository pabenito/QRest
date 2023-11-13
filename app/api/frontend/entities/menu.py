from typing import Optional

from app.core.entities.menu import Element, Section


class ExtendedElement(Element):
    quantity: Optional[int] = None
    clients: Optional[list[str]] = None


class ExtendedSection(Section):
    name: str
    visible: bool = True
    parent: Optional[str] = None
    elements: Optional[list[ExtendedElement]] = None
