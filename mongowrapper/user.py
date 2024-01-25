from pymongo.collection import Collection
from pymongo.database import Database

from mongowrapper.base import MongoBase
from mongowrapper.consts import DB_USER, DB_PSWD, DB_NAME


class MongoUser(MongoBase):
    def __init__(self, collection: str):
        super().__init__(DB_USER, DB_PSWD, DB_NAME)
        self.__collection = collection

    @property
    def db(self) -> Database:
        return self[DB_NAME]

    @property
    def collection(self) -> Collection:
        return self.db[self.__collection]


if __name__ == "__main__":
    root = MongoUser("logs")
    db = root.db
    db.drop_collection(root.collection)
    logs = root.collection
    logs.insert_one({"test": 1})
