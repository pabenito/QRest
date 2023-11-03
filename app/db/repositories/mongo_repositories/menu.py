from typing import Optional

from pymongo.client_session import ClientSession

from app import db
from app.core.entities.menu import Section
from app.db.repositories.interfaces.menu import IMenuRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.db.exceptions import PersistenceExceptionFactory


class MongoMenuRepository(IMenuRepository):
    def __init__(self):
        self.repository = MongoStandardRepository(
            collection="menu",
            exception_factory=PersistenceExceptionFactory("menu"))

    def get_all_sections(self, session: Optional[ClientSession] = None) -> list[Section]:
        result = self.repository.get_all_with_query_and_projection(
            does_not_have_attribute=["parent"],
            id_projection=False)
        return list(result).sort("name")

    def get_all_subsections(self, session: Optional[ClientSession] = None) -> list[Section]:
        result = self.repository.get_all_with_query_and_projection(
            has_attribute=["parent"],
            id_projection=False)
        return list(result).sort("name")
