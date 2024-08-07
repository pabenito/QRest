from typing import Optional
from abc import ABC, abstractmethod
from pymongo.client_session import ClientSession

from app.entities.menu import Section


class IMenuRepository(ABC):
    @abstractmethod
    def get_all(self, session: Optional[ClientSession] = None) -> list[Section]:
        pass

    @abstractmethod
    def get_all_sections(self, session: Optional[ClientSession] = None) -> list[Section]:
        pass

    @abstractmethod
    def get_all_subsections(self, session: Optional[ClientSession] = None) -> list[Section]:
        pass

    def section_element_exists(self, section: str, element: str) -> bool:
        pass
