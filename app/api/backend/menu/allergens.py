# Import libraries

from fastapi import APIRouter
from app.db import db
from app.core.entities.allergens import Allergen

# Create router
router = APIRouter()

# Collections
allergens = db["allergens"]


@router.get("/", response_model=list[Allergen])
def get():
    return list(allergens.find({}, {"_id": False}))


@router.get("/dict")
def get() -> dict:
    allergens_dict = {}
    for allergen in list(allergens.find({})):
        allergens_dict.update({allergen["name"]: allergen["icon"]})
    return allergens_dict