from datetime import datetime

from app.core.entities.order import Command, CommandPost
from app.db.repositories.interfaces.orders.commands import ICommandRepository


class CommandUseCases:
    def __init__(self, repository: ICommandRepository):
        self.repository = repository

    def add(self, order_id: str, command_post: CommandPost) -> Command:
        command = Command(**command_post.model_dump(), timestamp=datetime.now())
        return self.repository.add(order_id, command)

    def get_all(self, order_id: str) -> list[Command]:
        return self.repository.get_all(order_id)
