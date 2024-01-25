from pymongo.collection import Collection
from pymongo.database import Database

from mongowrapper.base import MongoBase
from mongowrapper.models import MongoOptions


class MongoUser(MongoBase):
    def __init__(self, options: MongoOptions, collection: str):
        self.__collection = collection
        super().__init__(options)

    @property
    def db(self) -> Database:
        return self[self.options.db_name]

    @property
    def collection(self) -> Collection:
        return self.db[self.__collection]


if __name__ == "__main__":
    _options = MongoOptions("test", "test", "test")
    root = MongoUser(_options, "logs")
    db = root.db
    db.drop_collection(root.collection)
    logs = root.collection
    logs.insert_one({"test": 1})
