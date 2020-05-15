from ..constants.Sys_Constants import car_status
from ..model.Car import Car
from ..model.Car import CarModel
from ..model.Car_Make import Car_Make
from ..model.Car_Make import CarMakeModel
from ..model.Record import RecordModel


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



