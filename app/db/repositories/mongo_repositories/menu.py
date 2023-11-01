from app.db import db
from app.core.entities.menu import Section
from app.db.repositories.interfaces.menu import IMenuRepository


class MongoMenuRepository(IMenuRepository):
    @staticmethod
    def _get_db():
        return db.get_collection("menu")

    def get_all_sections(self) -> list[Section]:
        return list(self._get_db().find({"parent": {"$exists": False}}, {"_id": False}).sort("name"))

    def get_all_subsections(self) -> list[Section]:
        return list(self._get_db().find({"parent": {"$exists": True}}, {"_id": False}).sort("name"))
