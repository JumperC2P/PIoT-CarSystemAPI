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

    def update_car(self, host, port, username, password, car):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': username,
            'password': password,
            'car': car
        }
        response = requests.post(host + ':' + port + "/updateCar", headers=headers, data=simplejson.dumps(data))
        return simplejson.loads(response.text)

    def remove_car(self, host, port, username, password, car_id):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': username,
            'password': password,
            'car_id': car_id
        }
        response = requests.post(host + ':' + port + "/removeCar", headers=headers, data=simplejson.dumps(data))
        return simplejson.loads(response.text)

    def report_car(self, host, port, username, password, report):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': username,
            'password': password,
            'car_id': report['car_id'],
            'issue': report['issue'],
            'admin_id': report['admin_id']
        }
        response = requests.post(host + ':' + port + "/reportCar", headers=headers, data=simplejson.dumps(data))
        return simplejson.loads(response.text)

    def close_report(self, host, port, username, password, close_report):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': username,
            'password': password,
            'car_id': close_report['car_id'],
            'report_id': close_report['report_id'],
            'engineer_id': close_report['engineer_id']
        }
        response = requests.post(host + ':' + port + "/closeReport", headers=headers, data=simplejson.dumps(data))
        return simplejson.loads(response.text)
