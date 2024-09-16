import logging
import os
import sys

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import OperationFailure

load_dotenv()
PSWD, HOST = os.getenv("PSWD"), os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "27017"))


class MongoAdmin(MongoClient):
    def __init__(self):
        super().__init__(HOST, PORT, username="root", password=PSWD, authSource="admin")

    def remove_user(self, user: str):
        self[user].command("dropUser", user)

    def create_user(self, user: str, pswd: str) -> bool:
        try:
            roles = [{"role": "readWrite", "db": user}]
            self[user].command("createUser", user, pwd=pswd, roles=roles)
            return True
        except OperationFailure as e:
            if "already exists" in str(e):
                r = input("Такой пользователь уже есть в БД, удалить его? (y/n): ")
                if r.lower() == "y":
                    self.remove_user(user)
                    self["customers"]["info"].find_one_and_delete({"name": user})
        return False

    def create_info_for_user(self, user: str, pswd: str, port: int):
        find_data = {"_id": port}
        data = {"_id": port, "name": user, "password": pswd}
        update_data = {"$set": {"name": user, "password": pswd}}
        if not self["customers"]["info"].find_one_and_update(find_data, update_data):
            self["customers"]["info"].insert_one(data)

    def main(self):
        user, pswd = sys.argv[1], sys.argv[2]
        if not user and not pswd:
            return print("Заполните аргументы: admin.py user pswd")
        try:
            if not self.create_user(user, pswd):
                return
        except Exception as e:
            return logging.exception(e)
        try:
            for options in self["customers"]["info"].find({}):
                port, name = options.get("_id"), options.get("name")
                print(f"Порт: {port} -> {name}")
            port = int(input("Введите порт: "))
            self.create_info_for_user(user, pswd, port)
        except Exception as e:
            logging.exception(e)


if __name__ == "__main__":
    MongoAdmin().main()
