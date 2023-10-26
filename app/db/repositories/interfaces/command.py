from app.core.entities.order import Element


class ICommandRepository:
    def add(self, order: str, element: Element) -> Element:
        pass

    def update(self, order: str, element: Element) -> Element:
        pass

    def remove(self, order: str, element: Element) -> Element:
        pass