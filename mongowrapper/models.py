from dataclasses import dataclass


@dataclass
class MongoOptions:
    user: str
    pswd: str
    db_name: str = ""
    host: str = "db1.yuharan.ru"
    port: int = 27017
    timeout: int = 60000

    def __post_init__(self):
        if not self.db_name:
            self.db_name = self.user
