from pydantic import BaseModel

from app.core.entities.order import Order, Element


class VersionedObject(BaseModel):
    version: int = 0


class DBElement(Element, VersionedObject):
    pass


class DBOrder(Order, VersionedObject):
    pass
