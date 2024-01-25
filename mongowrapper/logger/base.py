from datetime import datetime

from mongowrapper.logger.consts import T
from mongowrapper.models import MongoOptions
from mongowrapper.user import MongoUser


class MongoBaseLogger(MongoUser):
    def __init__(self, options: MongoOptions, collection: str):
        super().__init__(options, collection)

    @property
    def date(self) -> str:
        return datetime.utcnow().strftime("%F %T.%f")

    def debug(self, msg: str):
        message = {"_id": self.date, T.TYPE: T.DEBUG.value, T.MSG.value: msg}
        self.collection.insert_one(message)

    def info(self, msg: str):
        message = {"_id": self.date, T.TYPE: T.INFO.value, T.MSG.value: msg}
        self.collection.insert_one(message)

    def success(self, msg: str):
        message = {"_id": self.date, T.TYPE: T.SUCCESS.value, T.MSG.value: msg}
        self.collection.insert_one(message)

    def warning(self, msg: str):
        message = {"_id": self.date, T.TYPE: T.WARNING.value, T.MSG.value: msg}
        self.collection.insert_one(message)

    def error(self, msg: str):
        message = {"_id": self.date, T.TYPE: T.ERROR.value, T.MSG.value: msg}
        self.collection.insert_one(message)
