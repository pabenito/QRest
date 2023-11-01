import os
from typing import Mapping, Any

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

# Construye la ruta al archivo .env
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..', '.env')
env_path = os.path.abspath(env_path)  # obtén la ruta absoluta para eliminar cualquier '..'

# Carga las variables de entorno desde el archivo .env
load_dotenv(env_path)

db_uri = os.getenv("DB_URI")
db_name = os.getenv("DB_NAME")
db_client = None
db = None


def configure_db(testing: bool = False):
    global db_client, db
    if db_client is None:
        db_client = MongoClient(db_uri)
    if testing:
        db = db_client["test"]
    else:
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
