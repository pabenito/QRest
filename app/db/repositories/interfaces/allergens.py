from typing import Optional
from abc import ABC, abstractmethod
from pymongo.client_session import ClientSession

from app.extra.entities.allergens import Allergen


class IAllergensRepository(ABC):
    @abstractmethod
    def get_all(self, session: Optional[ClientSession] = None) -> list[Allergen]:
        pass
