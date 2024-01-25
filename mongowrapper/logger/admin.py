from typing import Optional

from mongowrapper.logger.base import MongoBaseLogger
from mongowrapper.logger.consts import T


class MongoAdminLogger(MongoBaseLogger):
    def __init__(self, app: Optional[str] = None):
        if app and not app.startswith("."):
            app = f".{app}"
        super().__init__(f"admin.logs{app if app else ''}")

    def exception(self, e: Exception):
        message = {
            "_id": self.date,
            T.TYPE.value: T.ERROR.value,
            T.MSG.value: f"{type(e)} {e}",
        }
        self.collection.insert_one(message)


if __name__ == "__main__":
    logger = MongoAdminLogger()
    try:
        raise ValueError("Error")
    except Exception as E:
        logger.exception(E)
