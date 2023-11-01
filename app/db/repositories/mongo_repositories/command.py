from app import db
from app.core.entities.order import Element
from app.db.repositories.interfaces.command import ICommandRepository


class MongoCommandRepository(ICommandRepository):
    @staticmethod
    def _get_db():
        return db.get_collection("order")

    def get_version(self, order: str, element: Element) -> int:
        pass

    def add(self, order: str, element: Element, version: int) -> Element:
        pass

    def update(self, order: str, element: Element, version: int) -> Element:
        pass

    def remove(self, order: str, element: Element, version: int) -> Element:
        pass
