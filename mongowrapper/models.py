from dataclasses import dataclass
from typing import Optional


@dataclass
class MongoOptions:
    user: str
    pswd: str
    db_name: Optional[str] = None
    host: str = "95.217.106.245"
    port: int = 27017

    def __post_init__(self):
        if not self.db_name:
            self.db_name = self.user
