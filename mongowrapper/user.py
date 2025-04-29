import contextlib

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.collection import Collection
from pymongo.database import Database

from mongowrapper.base import MongoAsyncBase, MongoBase
from mongowrapper.models import MongoOptions


class MongoUser(MongoBase):
    def __init__(self, options: MongoOptions, collection: str):
        self.__collection = collection
        super().__init__(options)

    @property
    def db(self) -> Database:
        return self._client[self._mongo_options.db_name]

    @property
    def collection(self) -> Collection:
        return self.db[self.__collection]

    def check_auth(self) -> bool:
        """Проверка авторизации"""
        with contextlib.suppress(Exception):
            self.collection.find_one({"_id": 1})
            return True
        return False


class MongoUserAsync(MongoAsyncBase):
    def __init__(self, options: MongoOptions, collection: str):
        self.__collection = collection
        super().__init__(options)

    @property
    def db(self) -> AsyncDatabase:
        return self._client[self._mongo_options.db_name]

    @property
    def collection(self) -> AsyncCollection:
        return self.db[self.__collection]

    async def check_auth(self) -> bool:
        """Проверка авторизации"""
        with contextlib.suppress(Exception):
            await self.collection.find_one({"_id": 1})
            return True
        return False
