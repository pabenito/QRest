from typing import Any

from app.core.entities.allergens import Allergen
from app.core.use_cases.command import CommandUseCases
from app.core.use_cases.menu import MenuUseCases
from app.core.use_cases.allergens import AllergensUseCases
from app.db.repositories.mongo_repositories.allergens import MongoAllergensRepository
from app.db.repositories.mongo_repositories.command import MongoCommandRepository
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.lib.utils import json_lower_encoder


class MenuFrontend:
    def __init__(self):
        self.menu_use_cases = MenuUseCases(repository=MongoMenuRepository())
        self.command_use_cases = CommandUseCases(order_repository=MongoOrderRepository(),
                                                 command_repository=MongoCommandRepository())
        self.allergens_use_cases = AllergensUseCases(repository=MongoAllergensRepository())
        self.encoder = json_lower_encoder

    @staticmethod
    def encode(object: Any) -> dict:
        return json_lower_encoder(object)

    def get_sections(self):
        return self.menu_use_cases.get_menu()

    def get_current_command(self, order_id: str):
        return self.command_use_cases.get(order_id)

    def get_allergens(self):
        return self.allergens_use_cases.get_allergens()

    def get_allergens_dict(self):
        return self._allergens_as_dict(self.get_allergens())

    @staticmethod
    def _allergens_as_dict(allergens: list[Allergen]):
        allergens_dict = dict()
        for allergen in allergens:
            allergens_dict.update({allergen.name: allergen.icon})
        return allergens_dict
