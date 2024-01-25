from typing import Optional

from pymongo.collection import Collection
from pymongo.database import Database

from mongowrapper.base import MongoBase
from mongowrapper.consts import DB_USER, DB_PSWD, DB_NAME


class MongoUser(MongoBase):
    def __init__(
        self,
        collection: str,
        user: Optional[str] = None,
        pswd: Optional[str] = None,
        db_name: Optional[str] = None,
    ):
        user, pswd = user if user else DB_USER, pswd if pswd else DB_PSWD
        self.__db_name = db_name if db_name else DB_NAME
        print(self.__db_name)
        print(DB_NAME, DB_USER, DB_PSWD)
        self.__collection = collection
        super().__init__(user, pswd, db_name)

    @property
    def db(self) -> Database:
        return self[self.__db_name]

    @property
    def collection(self) -> Collection:
        return self.db[self.__collection]


if __name__ == "__main__":
    root = MongoUser("logs")
    db = root.db
    db.drop_collection(root.collection)
    logs = root.collection
    logs.insert_one({"test": 1})
