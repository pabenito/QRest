from typing import Optional

from pymongo.client_session import ClientSession

from app.core.entities.menu import Section


class IMenuRepository:
    def get_all_sections(self, session: Optional[ClientSession] = None) -> list[Section]:
        pass

    def get_all_subsections(self, session: Optional[ClientSession] = None) -> list[Section]:
        pass
