from typing import Optional

from bson import ObjectId
from pymongo.client_session import ClientSession

from app import db
from app.core.exceptions import *
from app.core.entities.order import Element
from app.db.repositories.interfaces.command import ICommandRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.db.exceptions import PersistenceExceptionFactory


class MongoCommandRepository(ICommandRepository):
    def __init__(self):
        self.repository = MongoStandardRepository("order")

    def _element_match(self, element: Element) -> dict:
        element_dict = element.model_dump()
        if "quantity" in element_dict:
            del element_dict["quantity"]
        if "clients" in element_dict:
            del element_dict["clients"]
        return element_dict

    def get(self, order_id: str, element: Element, session: Optional[ClientSession] = None) -> Element:
        pass

    def exists(self, order_id: str, element: Element, session: Optional[ClientSession] = None) -> bool:
        return self.repository.has_element_in_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self._element_match(element), session=session)


def add(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        pass

    def update(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        pass

    def remove(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        pass
