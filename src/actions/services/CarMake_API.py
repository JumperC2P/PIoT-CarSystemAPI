from flask import Flask, Blueprint, request, jsonify, render_template
from ..model.Car_Make import Car_Make
from ..model.Car_Make import CarMakeSchema

car_make_api = Blueprint("car_make_api", __name__)

carMakeSchema = CarMakeSchema()
carMakesSchema = CarMakeSchema(many = True)

class CarMake_API:


    # Endpoint to show all people.
    @car_make_api.route("/car_make", methods = ["GET"])
    def getCarMake():
        user = Car_Make.query.all()
        result = carMakesSchema.dump(user)

        return jsonify(result)