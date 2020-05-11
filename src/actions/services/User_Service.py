import hashlib
from ..model.User import User
from ..model.User import UserModel

class User_Service:

    def login(self, username, password):
        return UserModel().login(username, password)

    def register(self, username, password, first_name, last_name, email, role):
        last_user_id = UserModel().getLastUserId()
        if (last_user_id):
            new_user_id = last_user_id+1
            return UserModel().add(new_user_id, username, password, first_name, last_name, email, role)
        else:
            return None

    def checkUserName(self, username):
        user = UserModel().checkUserName(username)
        print(user)
        for u in user:
            return False 
        return True