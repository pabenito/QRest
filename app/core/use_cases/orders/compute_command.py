from collections import defaultdict

from app.core.entities.order import Request, CommandPost, Element, Command, OrderElement
from app.core.exceptions.orders import OrderValidationException
from app.db.repositories.interfaces.orders.commands import ICommandRepository
from app.db.repositories.interfaces.orders.current_requests import ICurrentRequestsRepository
from app.db.repositories.interfaces.orders.processed_requests import IProcessedRequestsRepository
from app.core.use_cases.orders.commands import CommandUseCases
from app.core.use_cases.orders.current_requests import CurrentRequestsUseCases
from app.core.use_cases.orders.processed_requests import ProcessedRequestsUseCases
from app.lib.utils import json_lower_encoder


class ComputeCommandUseCases:
    def __init__(self,
                 commands_repository: ICommandRepository,
                 current_requests_repository: ICurrentRequestsRepository,
                 processed_requests_repository: IProcessedRequestsRepository):
        self.commands_use_cases = CommandUseCases(commands_repository)
        self.current_requests_use_cases = CurrentRequestsUseCases(current_requests_repository)
        self.processed_requests_use_cases = ProcessedRequestsUseCases(processed_requests_repository)
        self.json_encoder = json_lower_encoder

    def process_current_requests_and_create_new_command(self, order_id: str) -> Command:
        current_requests = self.current_requests_use_cases.get_all(order_id)
        command_post = self._compute_commands_from_requests(current_requests)
        command = self.commands_use_cases.add(order_id, command_post)
        self.processed_requests_use_cases.add_all(order_id, current_requests)
        self.current_requests_use_cases.remove_all(order_id)
        return command

    def _compute_commands_from_requests(self, requests: list[Request]) -> CommandPost:
        grouped_requests = defaultdict(int)
        for request in requests:
            key = (
                request.element.section,
                request.element.element,
                tuple(request.element.variants or None),
                tuple(request.element.extras or None),
                tuple(request.element.ingredients or None))
            if request.type == 'add':
                grouped_requests[key] += 1
            elif request.type == 'remove':
                grouped_requests[key] -= 1
            else:
                raise OrderValidationException(
                    f"The request.type mut be 'add' or 'remove', not '{request.type}'.")
        command_elements = []
        for key, quantity in grouped_requests.items():
            (section, element, variants, extras, ingredients) = key
            if quantity > 0:
                command_element = Element(
                    section=section,
                    element=element,
                    variants=variants,
                    extras=extras,
                    ingredients=ingredients)
                command_elements.append(OrderElement(
                    quantity=quantity,
                    element=self.json_encoder(command_element)))
        return CommandPost(elements=command_elements)
