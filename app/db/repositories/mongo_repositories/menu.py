from typing import Optional

from pymongo.client_session import ClientSession

from app.core.entities.menu import Section
from app.db.repositories.interfaces import IStandardRepository
from app.db.repositories.interfaces.menu import IMenuRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.lib.utils import parse_object


class MongoMenuRepository(IMenuRepository):
    def __init__(self):
        self.repository: IStandardRepository = MongoStandardRepository("menu")

    def get_all_sections(self, session: Optional[ClientSession] = None) -> list[Section]:
        result = self.repository.get_all_with_query_and_projection(
            does_not_have_attribute=["parent"],
            id_projection=False)
        section_list = list(result.sort("name"))
        return parse_object(list(section_list), list[Section])

    def get_all_subsections(self, session: Optional[ClientSession] = None) -> list[Section]:
        result = self.repository.get_all_with_query_and_projection(
            has_attribute=["parent"],
            id_projection=False)
        section_list = list(result.sort("name"))
        return parse_object(section_list, list[Section])
