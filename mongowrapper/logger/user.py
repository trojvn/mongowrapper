from mongowrapper.logger.base import MongoBaseLogger


class MongoUserLogger(MongoBaseLogger):
    def __init__(self):
        super().__init__("user.logs")
