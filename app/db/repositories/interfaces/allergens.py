from typing import Optional

from pymongo.client_session import ClientSession

from app.core.entities.allergens import Allergen


class IAllergensRepository:
    def get_all(self, session: Optional[ClientSession] = None) -> list[Allergen]:
        pass
