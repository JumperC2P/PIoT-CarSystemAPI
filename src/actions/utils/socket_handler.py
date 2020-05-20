import json
import socket
import time

from ..services.Car_Service import Car_Service


class Socket_Handler:
    """Socket_Handler is the entry point of socket connection."""

    def action_decider(self, data):
        """Endpoint to socket connection

        :param data the data sent from ap

        :return The result code for operations
        """
        result_code = 0
        if data['type'] == 1:  # facial recognition
            result_code = Car_Service().rent(False, data)
        elif data['type'] == 2:  # user authentication with username and password
            result_code = Car_Service().rent(True, data)
        elif data['type'] == 3:  # lock the car
            result_code = Car_Service().return_car(data)

        return result_code


if __name__ == '__main__':
    Socket_Handler().main()
