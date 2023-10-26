from app.core.entities.allergens import Allergen


class IAllergensRepository:
    def get_all(self) -> list[Allergen]:
        pass
