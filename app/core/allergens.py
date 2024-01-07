from app.extra.entities.allergens import Allergen
from app.db.repositories.interfaces.allergens import IAllergensRepository


class AllergensUseCases:
    def __init__(self, repository: IAllergensRepository):
        self.repository = repository

    def get_allergens(self) -> list[Allergen]:
        return self.repository.get_all()
