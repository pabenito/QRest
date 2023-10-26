from app.db import db
from app.core.entities.allergens import Allergen
from app.db.repositories.interfaces.allergens import IAllergensRepository


class MongoAllergensRepository(IAllergensRepository):
    def __init__(self):
        self.db = db["allergens"]

    def get_all(self) -> list[Allergen]:
        return list(self.db.find({}, {"_id": False}))
