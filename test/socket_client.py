import json
import time
from socket import *
import datetime as d
import socketio


class Socket_Client:

    def main(self):
        try:
            sio = socketio.Client()
            sio.connect('http://127.0.0.1:5000')

            message = [
                {"username": "Frank", "password": "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f",
                 "car_id": 5,
                 "time": d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"), "type": 2}]

            sio.emit('mp_socket', message)

            @sio.on('ap_socket')
            def rent_car(data):
                print(data)


        except ConnectionResetError as e:
            print("The Server is shutdown!!!\n Please wait !!!")
            time.sleep(5)
        except ConnectionAbortedError as c:
            print("The Server is shutdown!!!\n Please wait !!!")
            time.sleep(5)


if __name__ == '__main__':
    Socket_Client().main()
