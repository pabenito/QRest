from collections import Counter
from datetime import datetime

from pymongo.client_session import ClientSession

from app.core.entities.order import Command, Element, BasicElement
from app.core.use_cases.services.command import CommandServices
from app.db.exceptions import PersistenceExceptionFactory
from app.db.repositories.interfaces.order import IOrderRepository
from app.db.repositories.interfaces.command import ICommandRepository
from app.db.repositories.mongo_repositories import MongoTransactionManager
from app.core.exceptions import InvalidInputException


class CommandUseCases:
    def __init__(self, order_repository: IOrderRepository, command_repository: ICommandRepository):
        self.order_repository = order_repository
        self.command_repository = command_repository
        self.transaction_manager = MongoTransactionManager
        self.persistence_exception_factory = PersistenceExceptionFactory("order")
        self.services = CommandServices()

    def get(self, order_id: str) -> list[Element]:
        return self.order_repository.get_current_command(order_id)

    def confirm(self, order_id: str):
        with self.transaction_manager() as session:
            current_command = self.order_repository.get_current_command(order_id, session)
            new_command = Command(timestamp=datetime.now(), elements=current_command)
            self.order_repository.delete_current_command(order_id, session)
            self.order_repository.add_command(order_id, new_command, session)

    def update_element(self, order_id: str, element: Element) -> Element:
        self.services.check_element_is_correct(element)
        with self.transaction_manager() as session:
            if not self.command_repository.exists(order_id, self.services.element_to_basic_element(element), session):
                self.command_repository.add(order_id, element, session)
                return element
            db_element = self.command_repository.get(order_id, self.services.element_to_basic_element(element), session)
            self.services.update_db_element(db_element, element)
            self.command_repository.remove(order_id, self.services.element_to_basic_element(element), session)
            if db_element.quantity > 0:
                self.command_repository.add(order_id, db_element, session)
            return db_element