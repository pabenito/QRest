from typing import Any

from app.entities.frontend.menu import ExtendedSection, ExtendedElement
from app.api.services.extend_elment import generate_element_id_from_names
from app.entities.allergens import Allergen
from app.entities.menu import Section
from app.entities.order import Element
from app.use_cases.command import CommandUseCases
from app.use_cases.menu import MenuUseCases
from app.use_cases.allergens import AllergensUseCases
from app.use_cases.order import OrderUseCases
from app.db.repositories.mongo_repositories.allergens import MongoAllergensRepository
from app.db.repositories.mongo_repositories.command import MongoCommandRepository
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.extra.utils import json_lower_encoder


class MenuFrontend:
    def __init__(self):
        self.menu_use_cases = MenuUseCases(repository=MongoMenuRepository())
        self.order_use_cases = OrderUseCases(repository=MongoOrderRepository())
        self.command_use_cases = CommandUseCases(order_repository=MongoOrderRepository(),
                                                 command_repository=MongoCommandRepository())
        self.allergens_use_cases = AllergensUseCases(repository=MongoAllergensRepository())
        self.encoder = json_lower_encoder

    @staticmethod
    def encode(object: Any) -> dict:
        return json_lower_encoder(object)

    def create_order(self) -> str:
        return self.order_use_cases.create()

    def get_sections(self) -> list[Section]:
        return self.menu_use_cases.get_menu()

    def get_current_command(self, order_id: str) -> list[Element]:
        return self.command_use_cases.get(order_id)

    def get_allergens(self) -> list[Allergen]:
        return self.allergens_use_cases.get_allergens()

    def get_allergens_dict(self) -> dict:
        return self._allergens_as_dict(self.get_allergens())

    def get_extended_sections(self, order_id: str) -> list[ExtendedSection]:
        sections = self.get_sections()
        current_command = self.get_current_command(order_id)
        extended_sections = self.generate_extended_sections(sections, current_command)
        self._add_id_to_elements_in_sections(extended_sections)
        return extended_sections

    @staticmethod
    def _allergens_as_dict(allergens: list[Allergen]) -> dict:
        allergens_dict = dict()
        for allergen in allergens:
            allergens_dict.update({allergen.name: allergen.icon})
        return allergens_dict

    def generate_extended_sections(self, sections: list[Section], command: list[Element]) -> list[ExtendedSection]:
        extended_elements_dict = {}
        for element in command:
            if element.section not in extended_elements_dict:
                extended_elements_dict[element.section] = {}
            if element.element not in extended_elements_dict[element.section]:
                extended_elements_dict[element.section][element.element] = {}
                extended_elements_dict[element.section][element.element]["quantity"] = 0
                extended_elements_dict[element.section][element.element]["clients"] = []
            extended_elements_dict[element.section][element.element]["quantity"] += element.quantity
            extended_elements_dict[element.section][element.element]["clients"].extend(element.clients)
        extended_sections = []
        for section in sections:
            extended_section = ExtendedSection(name=section.name, visible=section.visible, parent=section.parent)
            extended_section.elements = []
            if section.elements:
                for element in section.elements:
                    extended_element = ExtendedElement(**self.encode(element))
                    if section.name in extended_elements_dict and element.name in extended_elements_dict[section.name]:
                        extended_element.quantity = extended_elements_dict[section.name][element.name]["quantity"]
                        extended_element.clients = extended_elements_dict[section.name][element.name]["clients"]
                    else:
                        extended_element.quantity = 0
                        extended_element.clients = []
                    extended_section.elements.append(extended_element)
            extended_sections.append(extended_section)
        return extended_sections

    def _add_id_to_elements_in_sections(self, extended_sections: list[ExtendedSection]):
        for section in extended_sections:
            for element in section.elements:
                element.id = generate_element_id_from_names(section.name, element.name)
