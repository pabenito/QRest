from typing import Optional

from pymongo.client_session import ClientSession

from app.entities.order import Element, BasicElement
from app.db.repositories.interfaces import IStandardRepository
from app.db.repositories.interfaces.command import ICommandRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.extra.utils import json_lower_encoder, parse_object


class MongoCommandRepository(ICommandRepository):
    def __init__(self):
        self.repository: IStandardRepository = MongoStandardRepository("orders")
        self.encoder = json_lower_encoder
        self.parse = parse_object

    def get(self, order_id: str, element: BasicElement, session: Optional[ClientSession] = None) -> Element:
        result = self.repository.get_from_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self.encoder(element),
            session=session)
        return self.parse(result, Element)

    def exists(self, order_id: str, element: BasicElement, session: Optional[ClientSession] = None) -> bool:
        return self.repository.has_element_in_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self.encoder(element),
            session=session)

    def add(self, order_id: str, element: Element, session: Optional[ClientSession] = None):
        self.repository.push_to_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self.encoder(element),
            session=session)

    def remove(self, order_id: str, element: BasicElement, session: Optional[ClientSession] = None):
        self.repository.pull_from_list_attribute(
            id=order_id,
            attribute="current_command",
            element=self.encoder(element),
            session=session)
