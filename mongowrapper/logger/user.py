from typing import Optional

from mongowrapper.logger.base import MongoBaseLogger


class MongoUserLogger(MongoBaseLogger):
    def __init__(self, app: Optional[str] = None):
        if app and not app.startswith("."):
            app = f".{app}"
        super().__init__(f"user.logs{app if app else ''}")
