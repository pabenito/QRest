import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Construye la ruta al archivo .env
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
env_path = os.path.abspath(env_path) # obtén la ruta absoluta para eliminar cualquier '..'

print(f"env_path: {env_path}")

# Carga las variables de entorno desde el archivo .env
load_dotenv(env_path)

db_uri = os.getenv("DB_URI")
db_name = os.getenv("DB_NAME")

print(f"DB_URI: {db_uri}")
print(f"DB_NAME: {db_name}")

db_client = MongoClient(db_uri)
db = db_client[db_name]