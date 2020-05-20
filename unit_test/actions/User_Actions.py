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


if __name__ == '__main__':
    User_Actions().login("http://127.0.0.1", "5000", "Frank", "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f")
