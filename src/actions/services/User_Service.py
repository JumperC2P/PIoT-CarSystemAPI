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

    def updatePassword(self, user_id, username, old_password, new_password):
        """Update user password

        In the method, it will check whether the user is valid or not, them update password

        :param user_id: user id:string
        :param old_password: username:string
        :param new_password: password:string
        """
        user = self.login(username, old_password)
        if user:
            UserModel().updatePassword(mysql323.hash(new_password), user_id)
            user['password'] = old_password
            return user
        else:
            return None

    def updateUser(self, user_id, a_username, a_password, first_name, last_name, email):
        """In the method, it will update user details into database.

        :param: user_id(string):  user id
        :param: username(string):  username
        :param: password(string):  password
        :param: first_name(string):  first name of the user
        :param: last_name(string):  last name of the user
        :param: email(string):  the user's email
        :param: role(string):  role of the user

        :return: the user object, if the user is added into the database.

        """
        user = self.login(a_username, a_password)
        if user:

            UserModel().update(user_id, first_name, last_name, email)

            user['first_name'] = first_name
            user['last_name'] = last_name
            user['email'] = email
            return user
        else:
            return None

    def checkUserName(self, username):
        """In the method, it will check whether or not the username is used.

        :param: username(string):  username

        :return: if the username is available , return True. If not, return False.

        """
        user = UserModel().checkUserName(username)
        for u in user:
            return dict(u)
        return None

    def getUsersWithparams(self, params):
        """In the method, it is used to get the user details which match the parameters.

        :param: params(JSON object): contains 5 parameters: role, username, first_name, last_name, email

        :return: a list of user details

        """
        params['username'] = "%"+params['username']+"%"
        params['first_name'] = "%"+params['first_name']+"%"
        params['last_name'] = "%"+params['last_name']+"%"
        params['email'] = "%"+params['email']+"%"

        return UserModel().getUsersWithparams(params)

    def deleteUser(self, user_id):
        UserModel().deleteUser(user_id)

    def find_by_mac_address(self, data):
        return UserModel().find_by_mac_address(data['mac_address'])

    def find_by_user_id(self, data):
        return UserModel().find_by_user_id(data['user_id'])
