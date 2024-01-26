from pymongo import MongoClient

from mongowrapper.models import MongoOptions


class MongoBase(MongoClient):
    def __init__(self, options: MongoOptions, admin: bool = False):
        self.__options = options
        super().__init__(
            host=options.host,
            port=options.port,
            username=options.user if not admin else options.root_user,
            password=options.pswd if not admin else options.root_pswd,
            authSource=options.db_name if not admin else options.root_db_name,
        )

    @property
    def mongo_options(self) -> MongoOptions:
        return self.__options
