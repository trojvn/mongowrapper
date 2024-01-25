from pymongo.errors import OperationFailure

from mongowrapper.base import MongoBase
from mongowrapper.models import MongoOptions


class MongoAdmin(MongoBase):
    def __init__(self, options: MongoOptions):
        super().__init__(options)

    def create_user(self):
        roles = [{"role": "readWrite", "db": self.mongo_options.db_name}]
        try:
            self[self.mongo_options.db_name].command(
                "createUser",
                self.mongo_options.user,
                pwd=self.mongo_options.pswd,
                roles=roles,
            )
        except OperationFailure as e:
            if "Authentication failed" in str(e):
                print("Не удалось авторизоваться!")
            elif "already exists" not in str(e):
                print(e)


if __name__ == "__main__":
    _options = MongoOptions("test", "test", "test", root_pswd="asd")
    MongoAdmin(_options).create_user()
