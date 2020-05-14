import hashlib
from ..model.User import User
from ..model.User import UserModel
from passlib.hash import mysql323


class User_Service:

    def login(self, username, password):
        hashedPassword = mysql323.hash(password)
        users = UserModel().login(username, hashedPassword)
        for u in users:
            return dict(u)
        return None

    def register(self, username, password, first_name, last_name, email, role):
        last_user_id = UserModel().getLastUserId()
        if last_user_id:
            new_user_id = last_user_id + 1
            return UserModel().add(new_user_id, username, mysql323.hash(password), first_name, last_name, email, role)
        else:
            return None

    def checkUserName(self, username):
        user = UserModel().checkUserName(username)
        print(user)
        for u in user:
            return False
        return True
