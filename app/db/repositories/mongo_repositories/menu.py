from typing import Optional

from pymongo.client_session import ClientSession

from app import db
from app.core.entities.menu import Section
from app.db.repositories.interfaces.menu import IMenuRepository


class MongoMenuRepository(IMenuRepository):
    @staticmethod
    def _get_db():
        return db.get_collection("menu")

    def get_all_sections(self, session: Optional[ClientSession] = None) -> list[Section]:
        return list(self._get_db().find(
            {"parent": {"$exists": False}},
            {"_id": False},
            session=session
        ).sort("name"))

    def get_all_subsections(self, session: Optional[ClientSession] = None) -> list[Section]:
        return list(self._get_db().find(
            {"parent": {"$exists": True}},
            {"_id": False},
            session=session
        ).sort("name"))
