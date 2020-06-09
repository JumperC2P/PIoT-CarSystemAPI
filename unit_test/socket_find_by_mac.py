import unittest
import simplejson
import socketio
import datetime as d


class Rent_Test(unittest.TestCase):

    def setUp(self):
        self._url = "http://127.0.0.1"
        # self._url = "http://192.168.1.72"
        self._port = "5000"
        self._user = {
            "username": "Test",
            "password": "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
        }

    def test_find_by_mac_address(self):
        message = [{"mac_address": "74:C1:4F:A6:DD:22", "type": 4}]

        try:
            sio = socketio.Client()
            sio.connect(self._url+":"+self._port)
            sio.emit('mp_socket', message)

            @sio.on('ap_socket')
            def socket_response(data):
                print(data)
                self.assertEqual(10, data[0]['Reason'])
                sio.disconnect()

            sio.wait()
            sio.disconnect()
        except ConnectionResetError as e:
            print("The Server is shutdown!!!\n Please wait !!!")
        except ConnectionAbortedError as c:
            print("The Server is shutdown!!!\n Please wait !!!")


if __name__ == '__main__':
    unittest.main()
