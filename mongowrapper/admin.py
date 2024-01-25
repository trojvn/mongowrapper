from typing import Optional

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
    """
    Чтобы добавить юзера ->
    DB_ROOT_USER (root),
    DB_ROOT_PSWD,
    DB_ROOT_NAME (admin)
    DB_USER,
    DB_PSWD,
    DB_NAME
    """

    def __init__(self):
        super().__init__(DB_ROOT_USER, DB_ROOT_PSWD, DB_ROOT_NAME)

    def create_user(
        self,
        user: Optional[str] = None,
        pswd: Optional[str] = None,
        db_name: Optional[str] = None,
    ):
        user, pswd = user if user else DB_USER, pswd if pswd else DB_PSWD
        db_name = db_name if db_name else DB_NAME
        roles = [{"role": "readWrite", "db": db_name}]
        try:
            self[db_name].command("createUser", user, pwd=pswd, roles=roles)
        except OperationFailure as e:
            if "Authentication failed" in str(e):
                print(f"Не удалось авторизоваться: {DB_ROOT_USER}:{DB_ROOT_PSWD}")
            elif "already exists" not in str(e):
                print(e)


if __name__ == "__main__":
    MongoAdmin().create_user()
