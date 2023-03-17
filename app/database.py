from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")
db_client = MongoClient(config["DB_URI"])
db = db_client[config["DB_NAME"]]