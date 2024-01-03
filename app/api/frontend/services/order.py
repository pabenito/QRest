from typing import Any

from app.api.frontend.entities.order import ExtendedElement
from app.api.services.extend_elment import generate_extend_elements_with_images
from app.core.entities.menu import Section
from app.core.entities.order import Element
from app.core.use_cases.command import CommandUseCases
from app.core.use_cases.menu import MenuUseCases
from app.core.use_cases.order import OrderUseCases
from app.core.use_cases.receipt import ReceiptUseCases
from app.db.repositories.mongo_repositories.command import MongoCommandRepository
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository
from app.db.repositories.mongo_repositories.order import MongoOrderRepository
from app.lib.utils import json_lower_encoder


class OrderFrontend:
    def __init__(self):
        self.menu_use_cases = MenuUseCases(repository=MongoMenuRepository())
        self.command_use_cases = CommandUseCases(order_repository=MongoOrderRepository(),
                                                 command_repository=MongoCommandRepository())
        self.receipt_use_cases = ReceiptUseCases(MongoOrderRepository, MongoMenuRepository)
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
        return generate_extend_elements_with_images(sections, current_command)

    def has_receipt(self, order_id: str):
        return self.receipt_use_cases.has(order_id)