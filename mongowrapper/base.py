import logging

from pymongo import AsyncMongoClient, MongoClient

from mongowrapper.models import MongoOptions


class MongoBase:
    def __init__(self, options: MongoOptions):
        self.__logger = logging.getLogger("mongowrapper")
        self._mongo_options = options
        self._client = self.__get_client()

    def __get_client(self) -> MongoClient:
        while True:
            try:
                return MongoClient(
                    host=self._mongo_options.host,
                    port=self._mongo_options.port,
                    username=self._mongo_options.user,
                    password=self._mongo_options.pswd,
                    authSource=self._mongo_options.db_name,
                    connectTimeoutMS=self._mongo_options.timeout,
                )
            except Exception as e:
                self.__logger.exception(e)


class MongoAsyncBase:
    def __init__(self, options: MongoOptions):
        self.__logger = logging.getLogger("mongowrapper")
        self._mongo_options = options
        self._client = self.__get_client()

    def __get_client(self) -> AsyncMongoClient:
        while True:
            try:
                return AsyncMongoClient(
                    host=self._mongo_options.host,
                    port=self._mongo_options.port,
                    username=self._mongo_options.user,
                    password=self._mongo_options.pswd,
                    authSource=self._mongo_options.db_name,
                    connectTimeoutMS=self._mongo_options.timeout,
                )
            except Exception as e:
                self.__logger.exception(e)
