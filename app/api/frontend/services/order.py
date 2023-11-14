from pprint import pprint
from typing import Any

from app.api.frontend.entities.order import ElementWithImage
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

    def get_current_command_elements_with_images(self, order_id: str) -> list[ElementWithImage]:
        sections = self.get_sections()
        current_command = self.get_current_command(order_id)
        return self.add_image_to_elements(sections, current_command)

    @staticmethod
    def add_image_to_elements(sections: list[Section], command: list[Element]) -> list[ElementWithImage]:
        image_dict = {}
        for section in sections:
            if section.elements is not None:
                for element in section.elements:
                    image_dict[(section.name, element.name)] = element.image
        elements_with_image = []
        for element in command:
            element_with_image = ElementWithImage(
                section=element.section,
                element=element.element,
                variants=element.variants,
                extras=element.extras,
                ingredients=element.ingredients,
                quantity=element.quantity,
                clients=element.clients,
                image=image_dict[(element.section, element.element)]
            )
            elements_with_image.append(element_with_image)
        return elements_with_image
