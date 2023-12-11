from collections import Counter

from app.db.exceptions import NotFoundException
from app.core.exceptions import InvalidInputException
from app.core.entities.order import Element, BasicElement
from app.db.repositories.interfaces.menu import IMenuRepository
from app.db.repositories.mongo_repositories.menu import MongoMenuRepository


class CommandServices:
    def __init__(self):
        self.menu_repository: IMenuRepository = MongoMenuRepository()

    def update_db_element(self, db_element: Element, element: Element):
        if element.quantity == 0:
            raise InvalidInputException("Element quantity for update cant be 0.")
        db_element.quantity += element.quantity
        if element.quantity > 0:
            db_element.clients.extend(element.clients)
        else:
            if not self._is_sublist_with_repetition(db_element.clients, element.clients):
                raise InvalidInputException(
                    f"Clients who request remove the element are not the ones who added it: {element.clients} are not in {db_element.clients}")
            db_element.clients = self._remove_sublist_with_repetition(db_element.clients, element.clients)

    @staticmethod
    def check_element_is_correct(element):
        if abs(element.quantity) != len(element.clients):
            raise InvalidInputException(
                f"Element quantity absolute value must be equals to clients list length. But element.quantity is {element.quantity} and element.clients is {element.clients}")

    @staticmethod
    def element_to_basic_element(element: Element) -> BasicElement:
        return BasicElement(
            section=element.section,
            element=element.element,
            variants=element.variants,
            extras=element.extras,
            ingredients=element.ingredients
        )

    @staticmethod
    def _is_sublist_with_repetition(original_list: list, sublist: list):
        original_list_frequencies = Counter(original_list)
        sublist_frequencies = Counter(sublist)
        for element, frequency in sublist_frequencies.items():
            if frequency > original_list_frequencies[element]:
                return False
        return True

    @staticmethod
    def _remove_sublist_with_repetition(original_list: list, sublist: list):
        sublist_frequencies = Counter(sublist)
        result_list = []
        for item in original_list:
            if sublist_frequencies[item] > 0:
                sublist_frequencies[item] -= 1
            else:
                result_list.append(item)
        return result_list

    def check_element_exists_in_menu(self, element: Element):
        if not self.menu_repository.section_element_exists(element.section, element.element):
            raise NotFoundException(f"Element does not exitst in menu: section:{element.section}, element:{element.element}")

