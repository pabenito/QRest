from app.db import db
from app.core.entities.order import Element
from app.db.repositories.interfaces.command import ICommandRepository


class MongoCommandRepository(ICommandRepository):
    def __init__(self):
        self.db = db["order"]

    def add(self, order: str, element: Element) -> Element:
        pass

    def update(self, order: str, element: Element) -> Element:
        pass

    def remove(self, order: str, element: Element) -> Element:
        pass
