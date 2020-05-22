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
