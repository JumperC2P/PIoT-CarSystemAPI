from ..model.Car import Car
from ..model.Car import CarModel
from ..model.Car_Make import Car_Make
from ..model.Car_Make import CarMakeModel
from ..model.Record import RecordModel
from datetime import datetime

class Car_Service:

    def getCarsWithMake(self):
        return CarModel().getCarsWithMake()

    def getMakes(self):
        return CarMakeModel().getCarMakes()
    
    def getSeatNumbers(self):
        return CarModel().getSeatNumbers()

    def getBodyTypes(self):
        return CarModel().getBodyTypes()

    def getColors(self):
        return CarModel().getColors()
    

    def getCarsWithparams(self, params):
        return CarModel().getCarsWithparams(params)

    def find_by_car_id(self, car_id):
        result = CarModel().find_by_car_id(car_id)
        for car in result:
            return dict(car)
        return None

    def book(self, book_info, user_id):
        est_rent_date = datetime.strptime(book_info['est_rent_date'], '%d/%m/%Y')
        est_return_date = datetime.strptime(book_info['est_return_date'], '%d/%m/%Y')
        return RecordModel().add(book_info['car_id'], est_rent_date, est_return_date, user_id)