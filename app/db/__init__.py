from typing import Mapping, Any

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from app.config import db_uri, db_name

db_client = None
db = None


def configure_db(testing: bool = False):
    global db_client, db
    if db_client is None:
        db_client = MongoClient(db_uri)
    if testing:
        print("Database is configured for testing")
        db = db_client["test"]
    else:
        print("Database is configured for deployment")
        db = db_client[db_name]


def get_client() -> MongoClient[Mapping[str, Any]]:
    if db_client is None:
        raise Exception("Database is not configured. Call configure_db first.")
    return db_client  # type: ignore


def get_db() -> Database[Mapping[str, Any]]:
    if db is None:
        raise Exception("Database is not configured. Call configure_db first.")
    return db  # type: ignore


def get_collection(collection: str) -> Collection[Mapping[str, Any]]:
    if db is None:
        raise Exception("Database is not configured. Call configure_db first.")
    return db[collection]  # type: ignore


def close():
    if isinstance(db_client, MongoClient):
        db_client.close()
