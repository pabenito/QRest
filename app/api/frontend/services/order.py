import hashlib
import json
from pprint import pprint
from typing import Any

from app.api.frontend.entities.order import ExtendedElement
from app.core.entities.menu import Section
from app.core.entities.order import Element
from app.core.use_cases.command import CommandUseCases
from app.core.use_cases.menu import MenuUseCases
from app.db.repositories.mongo_repositories.command import MongoCommandRepository
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.lib.utils import json_lower_encoder


class OrderFrontend:
    def __init__(self):
        self.menu_use_cases = MenuUseCases(repository=MongoMenuRepository())
        self.command_use_cases = CommandUseCases(order_repository=MongoOrderRepository(),
                                                 command_repository=MongoCommandRepository())
        self.encoder = json_lower_encoder

    @staticmethod
    def encode(object: Any) -> dict:
        return json_lower_encoder(object)

    def get_sections(self) -> list[Section]:
        return self.menu_use_cases.get_menu()

    def get_current_command(self, order_id: str) -> list[Element]:
        return self.command_use_cases.get(order_id)

    def get_current_command_with_extended_elements(self, order_id: str) -> list[ExtendedElement]:
        sections = self.get_sections()
        current_command = self.get_current_command(order_id)
        return self.extend_elements(sections, current_command)

    def extend_elements(self, sections: list[Section], command: list[Element]) -> list[ExtendedElement]:
        image_dict = {}
        for section in sections:
            if section.elements is not None:
                for element in section.elements:
                    image_dict[(section.name, element.name)] = element.image
        elements_with_image = []
        for element in command:
            extended_element = ExtendedElement(id=self.generate_element_id(element), **self.encode(element))
            extended_element.image = image_dict[(element.section, element.element)]
            elements_with_image.append(extended_element)
        return elements_with_image

    def generate_element_id(self, element: Element) -> str:
        json_str = json.dumps(self.encode(element), sort_keys=True)
        hash_obj = hashlib.sha256(json_str.encode())
        return hash_obj.hexdigest()
