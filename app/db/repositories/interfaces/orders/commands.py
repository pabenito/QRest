from app.core.entities.order import Command

class ICommandRepository:
    def add(self, order_id: str, command: Command) -> Command:
        pass

    def get_all(self, order_id: str) -> list[Command]:
        pass