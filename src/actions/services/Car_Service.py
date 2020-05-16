from .Record_Service import Record_Service
from ..constants.Sys_Constants import car_status
from ..model.Car import Car
from ..model.Car import CarModel
from ..model.Car_Make import Car_Make
from ..model.Car_Make import CarMakeModel
from ..model.Record import RecordModel
from .User_Service import User_Service


class Car_Service:
    """Car_Service is a logic layer of car actions."""

    def getCarsWithMake(self):
        """In the method, it is used to get all the cars information with manufacturer.
        """
        return CarModel().getCarsWithMake()

    def getMakes(self):
        """In the method, it is used to get all manufacturer.
        """
        return CarMakeModel().getCarMakes()

    def getSeatNumbers(self):
        """In the method, it is used to get all seat numbers.
        """
        return CarModel().getSeatNumbers()

    def getBodyTypes(self):
        """In the method, it is used to get all the body types.
        """
        return CarModel().getBodyTypes()

    def getColors(self):
        """In the method, it is used to get all the car color.
        """
        return CarModel().getColors()

    def getCarsWithparams(self, params):
        """In the method, it is used to get the car details which match the parameters.

        :param: params(JSON object): contains 4 list: make, seat numbers, body types, colors, which are the parameters of each factor

        :return: a list of car details

        """
        return CarModel().getCarsWithparams(params)

    def find_by_car_id(self, car_id):
        """In the method, it is used to get the car details which match the parameters.

        :param: car_id(int): car id

        :return: a dictionary object of the car

        """
        result = CarModel().find_by_car_id(car_id)
        for car in result:
            return dict(car)
        return None

    def rent(self, login, data):
        """In the method, it is used to rent the car

        :param: login(boolean): whether it need to login first
        :param: data(JSON object): the data sent from client ap

        :return: a number which represents different result

        """
        if login:
            user = User_Service().login(data['username'], data['password'])
            if user is None:
                return 3  # fail authentication
        else:
            user = User_Service().checkUserName(data['username'])
            if user is None:
                return 3  # fail authentication

        user_id = user['user_id']
        car_id = data['car_id']

        car = self.find_by_car_id(car_id)
        if car is None:
            return 4  # Cannot find the car
        elif car['car_status'] != car_status['B']:
            return 5  # The car is not under booking

        record = Record_Service().find_by_car_id_and_user_id_and_return_and_cancel(car_id, user_id, 0, 0)
        if record is None:
            return 6  # Cannot find the record.

        CarModel().update_status(car_id, car_status['R'])

        return 1  # The rental process is completed successfully.

    def return_car(self, data):
        """In the method, it is used to return the car

        :param: data(JSON object): the data sent from client ap

        :return: a number which represents different result

        """
        user = User_Service().checkUserName(data['username'])
        if user is None:
            return 3  # fail authentication

        user_id = user['user_id']
        car_id = data['car_id']

        car = self.find_by_car_id(car_id)
        if car is None:
            return 7  # Cannot find the car
        elif car['car_status'] != car_status['R']:
            return 8  # The car is not under rented

        record = Record_Service().find_by_car_id_and_user_id_and_return_and_cancel(car_id, user_id, 0, 0)
        if record is None:
            return 8  # Cannot find the record.

        CarModel().update_status(car_id, car_status['A'])

        RecordModel().update_is_return(record['record_id'], 1)

        return 2  # The return process is completed successfully.


