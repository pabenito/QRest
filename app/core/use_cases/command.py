from collections import Counter
from datetime import datetime

from pymongo.client_session import ClientSession

from app.core.entities.order import Command, Element, BasicElement
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.interfaces.command import ICommandRepository
from app.db.repositories.mongo_repositories import MongoTransactionManager
from app.core.exceptions import InvalidInputException


class CommandUseCases:
    def __init__(self, order_repository: IOrderRepository, command_repository: ICommandRepository):
        self.order_repository = order_repository
        self.command_repository = command_repository
        self.transaction_manager = MongoTransactionManager

    def get(self, order_id: str) -> list[Element]:
        return self.order_repository.get_current_command(order_id)

    def confirm(self, order_id: str):
        with self.transaction_manager() as session:
            current_command = self.order_repository.get_current_command(order_id, session)
            new_command = Command(timestamp=datetime.now(), elements=current_command)
            self.order_repository.delete_current_command(order_id, session)
            self.order_repository.add_command(order_id, new_command, session)

    def update_element(self, order_id: str, element: Element) -> Element:
        self._check_element_is_correct(element)
        with self.transaction_manager() as session:
            if not self.command_repository.exists(order_id, self.element_to_basic_element(element), session):
                self.command_repository.add(order_id, element, session)
                return element
            db_element = self.command_repository.get(order_id, self.element_to_basic_element(element), session)
            self._update_db_element(db_element, element)
            self.command_repository.remove(order_id, self.element_to_basic_element(element), session)
            if db_element.quantity > 0:
                self.command_repository.add(order_id, db_element, session)
            return db_element

    def _update_db_element(self, db_element: Element, element: Element):
        if element.quantity == 0:
            raise InvalidInputException("Element quantity for update cant be 0.")
        db_element.quantity += element.quantity
        if element.quantity > 0:
            db_element.clients.extend(element.clients)
        else:
            if not all(client in db_element.clients for client in element.clients):
                raise InvalidInputException(
                    f"Clients who request remove the element are not the ones who added it: {element.clients} are not in {db_element.clients}")
            db_element.clients = self._remove_sublist(db_element.clients, element.clients)

    @staticmethod
    def _check_element_is_correct(element):
        if abs(element.quantity) != len(element.clients):
            raise InvalidInputException(
                f"Element quantity absolute value must be equals to clients list length. But: element.quantity is {element.quantity} and element.clients is {element.clients}")

    @staticmethod
    def _remove_sublist(original_list: list, sublist: list):
        sublist_frequencies = Counter(sublist)
        result_list = []
        for item in original_list:
            if sublist_frequencies[item] > 0:
                sublist_frequencies[item] -= 1
            else:
                result_list.append(item)
        return result_list

    @staticmethod
    def element_to_basic_element(element: Element) -> BasicElement:
        return BasicElement(
            section=element.section,
            element=element.element,
            variants=element.variants,
            extras=element.extras,
            ingredients=element.ingredients
        )

