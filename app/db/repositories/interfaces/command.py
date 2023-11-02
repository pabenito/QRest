from app.core.entities.order import Element


class ICommandRepository:
    def get_version(self, order_id: str, element: Element) -> int:
        pass

    def add(self, order_id: str, element: Element, version: int):
        pass

    def update(self, order_id: str, element: Element, version: int) -> Element:
        pass

    def remove(self, order_id: str, element: Element, version: int):
        pass
