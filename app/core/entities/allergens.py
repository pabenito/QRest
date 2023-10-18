from pydantic import BaseModel, HttpUrl


class Allergen(BaseModel):
    name: str
    icon: HttpUrl