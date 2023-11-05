from typing import Optional
from pymongo.client_session import ClientSession

from app.core.entities.allergens import Allergen
from app.db.repositories.interfaces.allergens import IAllergensRepository
from app.db.repositories.mongo_repositories import MongoStandardRepository
from app.lib.utils import parse_object


class MongoAllergensRepository(IAllergensRepository):
    def __init__(self):
        self.repository = MongoStandardRepository("allergens")

    def get_all(self, session: Optional[ClientSession] = None) -> list[Allergen]:
        result = self.repository.get_all_with_query_and_projection(id_projection=False)
        return parse_object(list(result), list[Allergen])
