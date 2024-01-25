from dotenv import load_dotenv
from pymongo import MongoClient

from mongowrapper.consts import DB_HOST, DB_PORT

load_dotenv()


class MongoBase(MongoClient):
    def __init__(self, user: str, pswd: str, db: str):
        super().__init__(
            host=DB_HOST,
            port=DB_PORT,
            username=user,
            password=pswd,
            authSource=db,
        )
