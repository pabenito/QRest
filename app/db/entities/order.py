from pydantic import BaseModel

from app.core.entities.order import Order, Element


class VersionedObject(BaseModel):
    version: int = 0


class VersionedElement(Element, VersionedObject):
    pass


class VersionedOrder(Order, VersionedObject):
    pass
