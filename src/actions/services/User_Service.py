import hashlib
from ..model.User import User
from ..model.User import UserModel

class User_Service:

    def login(self, username, password):
        h = hashlib.new("sha256",password.encode('utf-8'))
        print(username)
        print(password)
        print(h.hexdigest())

        return UserModel().login(username, password)