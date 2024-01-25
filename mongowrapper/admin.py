from pymongo.errors import OperationFailure

from mongowrapper.base import MongoBase
from mongowrapper.consts import (
    DB_NAME,
    DB_USER,
    DB_PSWD,
    DB_ROOT_NAME,
    DB_ROOT_PSWD,
    DB_ROOT_USER,
)


class MongoAdmin(MongoBase):
    def __init__(self):
        super().__init__(DB_ROOT_USER, DB_ROOT_PSWD, DB_ROOT_NAME)

    def create_user(self):
        roles = [{"role": "readWrite", "db": DB_NAME}]
        try:
            self[DB_NAME].command("createUser", DB_USER, pwd=DB_PSWD, roles=roles)
        except OperationFailure as e:
            if "Authentication failed" in str(e):
                print(f"Не удалось авторизоваться: {DB_ROOT_USER}:{DB_ROOT_PSWD}")
            elif "already exists" not in str(e):
                print(e)


if __name__ == "__main__":
    MongoAdmin().create_user()
