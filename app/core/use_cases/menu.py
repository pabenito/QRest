from pprint import pprint

from app.core.entities.menu import Section
from app.core.use_cases.services.menu import MenuServices
from app.db.repositories.interfaces.menu import IMenuRepository


class MenuUseCases:
    def __init__(self, repository: IMenuRepository):
        self.repository = repository
        self.services = MenuServices()

    def get_menu(self) -> list[Section]:
        sections = self.repository.get_all_sections()
        subsections = self.repository.get_all_subsections()
        return self.services.sort_menu(sections, subsections)
