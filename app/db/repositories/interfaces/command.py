from typing import Optional
from abc import ABC, abstractmethod
from pymongo.client_session import ClientSession

from app.core.entities.order import Element, BasicElement


class ICommandRepository(ABC):
    @abstractmethod
    def get(self, order_id: str, element: BasicElement, session: Optional[ClientSession] = None) -> Element:
        pass

    @abstractmethod
    def exists(self, order_id: str, element: BasicElement, session: Optional[ClientSession] = None) -> bool:
        pass

    @abstractmethod
    def add(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def remove(self, order_id: str, element: BasicElement, session: Optional[ClientSession] = None):
        pass
