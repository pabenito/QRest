from app.core.entities.order import Element


class ICommandRepository:
    def exists(self, order_id: str, element: Element):
        pass

    def add(self, order_id: str, element: Element):
        pass

    def update(self, order_id: str, element: Element) -> Element:
        pass

    def remove(self, order_id: str, element: Element):
        pass
