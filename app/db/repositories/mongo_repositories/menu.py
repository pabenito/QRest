from typing import Optional

from pymongo.client_session import ClientSession

from app.extra.entities.menu import Section
from app.db.repositories.interfaces import IStandardRepository
from app.db.repositories.interfaces.menu import IMenuRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.extra.utils import parse_object


class MongoMenuRepository(IMenuRepository):
    def __init__(self):
        self.repository: IStandardRepository = MongoStandardRepository("menu")

    def get_all(self, session: Optional[ClientSession] = None) -> list[Section]:
        result = self.repository.get_all_with_query_and_projection(
            id_projection=False,
            session=session)
        section_list = list(result.sort("name"))
        return parse_object(list(section_list), list[Section])

    def get_all_sections(self, session: Optional[ClientSession] = None) -> list[Section]:
        result = self.repository.get_all_with_query_and_projection(
            does_not_have_attribute=["parent"],
            id_projection=False,
            session=session)
        section_list = list(result.sort("name"))
        return parse_object(list(section_list), list[Section])

    def get_all_subsections(self, session: Optional[ClientSession] = None) -> list[Section]:
        result = self.repository.get_all_with_query_and_projection(
            has_attribute=["parent"],
            id_projection=False,
            session=session)
        section_list = list(result.sort("name"))
        return parse_object(section_list, list[Section])

    def section_element_exists(self, section: str, element: str, session: Optional[ClientSession] = None) -> bool:
        result = self.repository.get_with_query_and_projection(
            has_attribute_value={"name": section},
            has_list_value={"elements": {"name": element}},
            session=session)
        return True if result else False
