import requests
import simplejson


class Car_Actions:

    def show_available_cars(self, host, port, username, password, params):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': username,
            'password': password,
            'params': params
        }
        response = requests.post(host + ':' + port + "/getCarsWithparams", headers=headers, data=simplejson.dumps(data))
        return simplejson.loads(response.text)
