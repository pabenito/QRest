import os

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
env_path = os.path.abspath(env_path)
load_dotenv(env_path)

db_uri = os.getenv("DB_URI")
db_name = os.getenv("DB_NAME")
url = os.getenv("URL")
