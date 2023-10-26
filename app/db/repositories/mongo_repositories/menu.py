from app.db import db
from app.core.entities.menu import Section
from app.db.repositories.interfaces.menu import IMenuRepository
from app.lib.utils import json_lower_encoder


class MongoMenuRepository(IMenuRepository):
    def __init__(self):
        self.db = db["menu"]
        self.json_encoder = json_lower_encoder

    def get_all_sections(self) -> list[Section]:
        return list(self.db.find({"parent": {"$exists": False}}, {"_id": False}).sort("name"))

    def get_all_subsections(self) -> list[Section]:
        return list(self.db.find({"parent": {"$exists": True}}, {"_id": False}).sort("name"))
