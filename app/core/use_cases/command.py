from pydantic import TypeAdapter
from datetime import datetime

from app.core.entities.order import Command, Element
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.interfaces.command import ICommandRepository


class CommandUseCases:
    def __init__(self, order_repository: IOrderRepository, command_repository: ICommandRepository):
        self.order_repository = order_repository
        self.command_respository = command_repository

    def get(self, order: str) -> list[Element]:
        return self.order_repository.get_attribute(order, "current_command", list[Element])

    def confirm(self, order: str) -> Command:
        current_command = self.get(order)
        commands: list[Command] = self.order_repository.get_attribute(order, "commands", list[Command])
        if commands is None:
            self.order_repository.add_attribute(order, "commands", [])
            commands = []
        new_command = Command(timestamp=datetime.now(), elements=current_command)
        commands.append(new_command)
        self.order_repository.add_attribute(order, "commands", commands)
        return new_command

    def update_element(self, order: str, element: Element) -> Element:
        current_command = self.get(order)
        for command_element in current_command:
            if command_element.section == element.section and command_element.element == element.element and command_element.extras == element.extras and command_element.variants == element.variants and command_element.ingredients == element.ingredients:
                command_element.quantity += element.quantity
                break






