from typing import Optional

from pydantic import HttpUrl

from app.core.entities.order import Element


class ExtendedElement(Element):
    id: Optional[str] = None
    image: Optional[HttpUrl] = None
