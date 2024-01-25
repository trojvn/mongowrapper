import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 27017))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PSWD = os.getenv("DB_PSWD")

DB_ROOT_NAME = os.getenv("DB_ROOT_NAME", "admin")
DB_ROOT_USER = os.getenv("DB_ROOT_USER", "root")
DB_ROOT_PSWD = os.getenv("DB_ROOT_PSWD")
