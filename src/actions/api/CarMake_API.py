from flask import Flask, Blueprint, request, jsonify, render_template
from ..model.Car_Make import Car_Make
from ..model.Car_Make import CarMakeModel

car_make_api = Blueprint("car_make_api", __name__)


class CarMake_API:

    # Endpoint to show all people.
    @car_make_api.route("/car_make", methods = ["GET"])
    def getCarMake():
        result = CarMakeModel().getCarMake()

        return jsonify(result)