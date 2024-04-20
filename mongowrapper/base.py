from pymongo import MongoClient

from mongowrapper.models import MongoOptions


class MongoBase(MongoClient):
    def __init__(self, options: MongoOptions):
        self.__options = options
        super().__init__(
            host=options.host,
            port=options.port,
            username=options.user,
            password=options.pswd,
            authSource=options.db_name,
        )

    @property
    def mongo_options(self) -> MongoOptions:
        return self.__options
