from pymongo import MongoClient

from mongowrapper.models import MongoOptions


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
                    connectTimeoutMS=60000,
                )
                break
            except Exception:
                pass

    @property
    def mongo_options(self) -> MongoOptions:
        return self.__mongo_options
