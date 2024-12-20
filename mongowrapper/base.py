import logging

from pymongo import MongoClient

from .models import MongoOptions


class MongoBase(MongoClient):
    def __init__(self, options: MongoOptions):
        self.__mongo_options = options
        while True:
            try:
                super().__init__(
                    host=options.host,
                    port=options.port,
                    username=options.user,
                    password=options.pswd,
                    authSource=options.db_name,
                    connectTimeoutMS=options.timeout,
                )
                break
            except Exception as e:
                logging.exception(e)

    @property
    def mongo_options(self) -> MongoOptions:
        return self.__mongo_options
