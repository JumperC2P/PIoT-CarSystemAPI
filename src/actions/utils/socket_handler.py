import simplejson as json
import socket
import time

from src.actions.services.User_Service import User_Service
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
            message = [{"Reason": result_code}]
        elif data['type'] == 2:  # user authentication with username and password
            result_code = Car_Service().rent(True, data)
            message = [{"Reason": result_code}]
        elif data['type'] == 3:  # lock the car
            result_code = Car_Service().return_car(data)
            message = [{"Reason": result_code}]
        elif data['type'] == 4:  # find engineer with MAC
            user = User_Service().find_by_mac_address(data)
            if user:
                user['password'] = ""
                message = [{"Reason": 9, "user": user}]
            else:
                message = [{"Reason": 10}]
        elif data['type'] == 5:  # voice find car
            cars = Car_Service().find_by_make(data)
            if cars:
                cars = [dict(c) for c in cars]
                message = [{"Reason": 11, "cars": json.dumps(cars, use_decimal=True)}]
            else:
                message = [{"Reason": 12}]
        elif data['type'] == 6:  # QR code get enginner
            user = User_Service().find_by_user_id(data)
            if user:
                user['password'] = ""
                message = [{"Reason": 13, "user": user}]
            else:
                message = [{"Reason": 14}]

        return message


if __name__ == '__main__':
    Socket_Handler().main()
