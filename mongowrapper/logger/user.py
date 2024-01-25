from typing import Optional

from mongowrapper.logger.base import MongoBaseLogger
from mongowrapper.models import MongoOptions


class MongoUserLogger(MongoBaseLogger):
    def __init__(self, options: MongoOptions, app: Optional[str] = None):
        if app and not app.startswith("."):
            app = f".{app}"
        super().__init__(options, f"user.logs{app if app else ''}")
