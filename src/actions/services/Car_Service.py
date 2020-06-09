from .Record_Service import Record_Service
from .Report_Service import Report_Service
from ..constants.Sys_Constants import car_status
from ..model.Car import Car
from ..model.Car import CarModel
from ..model.Car_Make import Car_Make
from ..model.Car_Make import CarMakeModel
from .User_Service import User_Service
from ..model.Record import RecordModel
from ..utils.Pushbullet_utils import Pushbullet_utils


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

    def addCar(self, car):
        """In the method, it is used to add a car

        :param: car(JSON object): the car object

        :return: the car object

        """
        return CarModel().add(int(car['cost']), car['make'], car['body_type'], car['seat_number'], car['car_location'], car['color'])

    def updateCar(self, car):
        """Update car details"""
        CarModel().updateCar(car['car_id'], car['cost'], car['make'], car['body_type'], car['seat_number'], car['car_location'], car['color'])

    def removeCar(self, car_id):
        """Remove car from database"""
        CarModel().removeCar(int(car_id))

    def reportCar(self, car_id, admin_id, issue):
        """
        Report issues of cars
        :param car_id: car id
        :param admin_id: who report the issue
        :param issue: issue
        """
        CarModel().update_status(car_id, car_status['P'])
        Report_Service().add(car_id, admin_id, issue)
        self.send_pushbullet_with_report_info()

    def send_pushbullet_with_report_info(self):
        """
        Send notification via Pushbullet API
        """
        report = Report_Service().find_the_new_one()
        title = 'A car has been reported with issue.'
        message = 'The details of the report:\nReport ID: ' + str(report.report_id) + '\nCar ID: ' + str(report.car_id) + '\nMake: ' + report.name + '\nBody Type: ' + report.body_type + '\nCar Location: http://maps.google.com/maps?q=' + report.car_location + '&z=18\nIssue: ' + report.issue
        Pushbullet_utils().send_notification_via_pushbullet(title, message)

    def find_by_make(self, data):
        params = dict()
        params['makes'] = [data['name'].lower().capitalize()]
        params['status'] = []
        params['colors'] = []
        params['types'] = []
        params['seats'] = []
        return self.getCarsWithparams(params)


