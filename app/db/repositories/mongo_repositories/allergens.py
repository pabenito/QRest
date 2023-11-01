from app import db
from app.core.entities.allergens import Allergen
from app.db.repositories.interfaces.allergens import IAllergensRepository


class MongoAllergensRepository(IAllergensRepository):
    @staticmethod
    def _get_db():
        return db.get_collection("allergens")

    def get_all(self) -> list[Allergen]:
        return list(self._get_db().find({}, {"_id": False}))
