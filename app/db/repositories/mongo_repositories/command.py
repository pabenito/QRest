from typing import Optional

from bson import ObjectId

from app import db
from app.core.exceptions import *
from app.core.entities.order import Element
from app.db.repositories.interfaces.command import ICommandRepository
from app.db.repositories.mongo_repositories import OptionalOCCRepository, MongoStandardRepository, MongoOCCRepository


class MongoCommandRepository(ICommandRepository):
    def __init__(self):
        self.repository = OptionalOCCRepository(
            standard_repository=MongoStandardRepository("order"),
            occ_repository=MongoOCCRepository("order"))

    @staticmethod
    def _get_db():
        return db.get_collection("order")

    @staticmethod
    def _elem_match_condition(element: Element):
        elem_match_condition = {"section": element.section, "element": element.element}
        if element.variants is not None:
            elem_match_condition["variants"] = {"$all": [variant.model_dump() for variant in element.variants]}
        if element.extras is not None:
            elem_match_condition["extras"] = {"$all": [extra for extra in element.extras]}
        if element.ingredients is not None:
            elem_match_condition["ingredients"] = {"$all": [ingredient for ingredient in element.ingredients]}
        return elem_match_condition

    def exists(self, order_id: str, element: Element) -> bool:
        result = self._get_db().find_one(
            {"_id": ObjectId(order_id), "current_command": {"$elemMatch": self._elem_match_condition(element)}},
            {"current_command.$": True})
        if not result or 'current_command' not in result or len(result['current_command']) == 0:
            return False
        return True

    def add(self, order_id: str, element: Element):
        self.repository.push_attribute(order_id, "current_command", element)

    def update(self, order_id: str, element: Element) -> Element:
        self

    def remove(self, order_id: str, element: Element):
        self.repository.pop_attribute(order_id, "current_command", element)
