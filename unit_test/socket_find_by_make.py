import unittest
import simplejson
import socketio
import datetime as d


class Rent_Test(unittest.TestCase):

    def setUp(self):
        self._url = "http://127.0.0.1"
        # self._url = "http://192.168.1.72"
        self._port = "5000"

    def test_find_by_user_id(self):
        message = [{"name": "honda", "type": 5}]

        try:
            sio = socketio.Client()
            sio.connect(self._url+":"+self._port)
            sio.emit('mp_socket', message)

            @sio.on('ap_socket')
            def socket_response(data):
                print(data)
                self.assertEqual(12, data[0]['Reason'])
                sio.disconnect()

            sio.wait()
            sio.disconnect()
        except ConnectionResetError as e:
            print("The Server is shutdown!!!\n Please wait !!!")
        except ConnectionAbortedError as c:
            print("The Server is shutdown!!!\n Please wait !!!")


if __name__ == '__main__':
    unittest.main()
