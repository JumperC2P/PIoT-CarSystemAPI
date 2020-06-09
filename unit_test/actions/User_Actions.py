import requests
import simplejson


class User_Actions:

    def login(self, host, port, username, password):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(host+':'+port+"/login", headers=headers, data=data)
        return simplejson.loads(response.text)

    def register(self, host, port, user):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(host+':'+port+"/register", headers=headers, data=user)
        return simplejson.loads(response.text)

    def update_user(self, host, port, username, password, update_user):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'user_id': update_user['user_id'],
            'a_username': username,
            'a_password': password,
            'first_name': update_user['first_name'],
            'last_name': update_user['last_name'],
            'email': update_user['email']
        }
        response = requests.post(host+':'+port+"/updateUser", headers=headers, data=data)
        return simplejson.loads(response.text)

    def remove_user(self, host, port, username, password, user_id):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'user_id': user_id,
            'username': username,
            'password': password
        }
        response = requests.post(host+':'+port+"/deleteUser", headers=headers, data=simplejson.dumps(data))
        return simplejson.loads(response.text)
