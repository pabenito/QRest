from app.core.entities.order import Element


class ICommandRepository:
    def get_version(self, order: str, element: Element) -> int:
        pass

    def add(self, order: str, element: Element, version: int) -> Element:
        pass

    def update(self, order: str, element: Element, version: int) -> Element:
        pass

    def remove(self, order: str, element: Element, version: int) -> Element:
        pass
