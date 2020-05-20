import requests
import simplejson


class Record_Actions:

    def cancel(self, host, port, username, password, record):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': username,
            'password': password,
            'record': record
        }
        response = requests.post(host + ':' + port + "/cancel_booking", headers=headers, data=simplejson.dumps(data))
        print(response.text)
        return simplejson.loads(response.text)

    def book(self, host, port, username, password, book_info):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': username,
            'password': password,
            'book_info': book_info
        }
        response = requests.post(host + ':' + port + "/book", headers=headers, data=simplejson.dumps(data))
        return simplejson.loads(response.text)

    def show_history(self, host, port, username, password):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': username,
            'password': password,
        }
        response = requests.post(host + ':' + port + "/getRecords", headers=headers, data=simplejson.dumps(data))
        return simplejson.loads(response.text)



if __name__ == '__main__':
    Record_Actions().show_history("http://127.0.0.1", "5000", "Frank",
                            "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f")
