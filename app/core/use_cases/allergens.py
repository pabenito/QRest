from app.core.entities.allergens import Allergen
from app.db.repositories.interfaces.allergens import IAllergensRepository


def _allergens_as_dict(allergens: list[Allergen]):
    allergens_dict = dict()
    for allergen in allergens:
        allergens_dict.update({allergen.name: allergen.icon})
    return allergens_dict


class AllergensUseCases:
    def __init__(self, repository: IAllergensRepository):
        self.repository = repository

    def get_allergens_dict(self) -> dict:
        allergens = self.repository.get_all()
        return _allergens_as_dict(allergens)