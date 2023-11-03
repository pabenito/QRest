from typing import Optional

from pymongo.client_session import ClientSession

from app.core.entities.order import Element


class ICommandRepository:
    def get(self, order_id: str, element: Element, session: Optional[ClientSession] = None) -> Element:
        pass

    def exists(self, order_id: str, element: Element, session: Optional[ClientSession] = None) -> bool:
        pass

    def add(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        pass

    def update(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        pass

    def remove(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        pass
