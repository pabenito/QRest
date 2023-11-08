from typing import Optional

from pydantic import HttpUrl

from app.core.entities.order import Element


class ElementWithImage(Element):
    image: Optional[HttpUrl] = None
