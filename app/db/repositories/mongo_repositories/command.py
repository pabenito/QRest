from typing import Optional

from bson import ObjectId
from pymongo.client_session import ClientSession

from app import db
from app.core.exceptions import *
from app.core.entities.order import Element
from app.db.repositories.interfaces.command import ICommandRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.db.exceptions import PersistenceExceptionFactory
from app.lib.utils import json_lower_encoder, parse_object


class MongoCommandRepository(ICommandRepository):
    def __init__(self):
        self.repository = MongoStandardRepository("order")
        self.encoder = json_lower_encoder
        self.parse = parse_object

    def _element_match(self, element: Element) -> dict:
        element_dict = self.encoder(element)
        if "quantity" in element_dict:
            del element_dict["quantity"]
        if "clients" in element_dict:
            del element_dict["clients"]
        return element_dict

    def get(self, order_id: str, element: Element, session: Optional[ClientSession] = None) -> Element:
        result = self.repository.get_from_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self._element_match(element),
            session=session)
        return self.parse(result, Element)

    def exists(self, order_id: str, element: Element, session: Optional[ClientSession] = None) -> bool:
        return self.repository.has_element_in_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self._element_match(element),
            session=session)

    def add(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        self.repository.push_to_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self._element_match(element),
            session=session)

    def remove(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        self.repository.pull_from_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self._element_match(element),
            session=session)
