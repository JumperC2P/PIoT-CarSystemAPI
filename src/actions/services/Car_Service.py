from ..model.Car import Car
from ..model.Car import CarModel
from ..model.Car_Make import Car_Make
from ..model.Car_Make import CarMakeModel

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
    