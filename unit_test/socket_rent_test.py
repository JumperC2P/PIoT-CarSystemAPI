import unittest
import simplejson
import socketio
import datetime as d


class Rent_Test(unittest.TestCase):

    def setUp(self):
        self._url = "http://192.168.1.72"
        self._port = "5000"
        self._user = {
            "username": "Test",
            "password": "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
        }

    def test_rent(self):
        message = [{"username": self._user['username'], "car_id": 4,
                    "time": d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"), "type": 1}]

        try:
            sio = socketio.Client()
            sio.connect(self._url+":"+self._port)
            sio.emit('mp_socket', message)

            @sio.on('ap_socket')
            def socket_response(data):
                self.assertEqual(1, data[0]['Reason'])
                sio.disconnect()

            sio.wait()
            sio.disconnect()
        except ConnectionResetError as e:
            print("The Server is shutdown!!!\n Please wait !!!")
        except ConnectionAbortedError as c:
            print("The Server is shutdown!!!\n Please wait !!!")


if __name__ == '__main__':
    unittest.main()
