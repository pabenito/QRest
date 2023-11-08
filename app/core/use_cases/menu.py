from pprint import pprint

from app.core.entities.menu import Section
from app.db.repositories.interfaces.menu import IMenuRepository


def _sort_menu(sections: list[Section], subsections: list[Section]):
    sections_with_subsections = {section.name: [] for section in sections}
    for subsection in subsections:
        sections_with_subsections[subsection.parent].append(subsection)
    ordered_menu = []
    for section in sections:
        ordered_menu.append(section)
        ordered_menu.extend(sections_with_subsections[section.name])
    return ordered_menu


class MenuUseCases:
    def __init__(self, repository: IMenuRepository):
        self.repository = repository

    def get_menu(self) -> list[Section]:
        sections = self.repository.get_all_sections()
        subsections = self.repository.get_all_subsections()
        return _sort_menu(sections, subsections)
