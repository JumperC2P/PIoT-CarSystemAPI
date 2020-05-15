import hashlib
from ..model.User import User
from ..model.User import UserModel
from passlib.hash import mysql323


class User_Service:
    """User_Service is a logic layer of user actions."""

    def login(self, username, password):
        """In the method, it will use the username and password encrypted to query whether or not the user is exist.

        :param: username(string): login username
        :param: password(string): login password

        :return: the user object, if the user is exist or the authentication is valid.

        """
        hashedPassword = mysql323.hash(password)
        users = UserModel().login(username, hashedPassword)
        for u in users:
            return dict(u)
        return None

    def register(self, username, password, first_name, last_name, email, role):
        """In the method, it will add a new user into database.

        :param: username(string):  username
        :param: password(string):  password
        :param: first_name(string):  first name of the user
        :param: last_name(string):  last name of the user
        :param: email(string):  the user's email
        :param: role(string):  role of the user

        :return: the user object, if the user is added into the database.

        """
        last_user_id = UserModel().getLastUserId()
        if last_user_id:
            new_user_id = last_user_id + 1
            return UserModel().add(new_user_id, username, mysql323.hash(password), first_name, last_name, email, role)
        else:
            return None

    def checkUserName(self, username):
        """In the method, it will check whether or not the username is used.

        :param: username(string):  username

        :return: if the username is available , return True. If not, return False.

        """
        user = UserModel().checkUserName(username)
        print(user)
        for u in user:
            return False
        return True
