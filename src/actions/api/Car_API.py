from flask import Flask, Blueprint, request, jsonify, render_template
from ..model.Car import Car
from ..model.Car import CarModel

car_api = Blueprint("car_api", __name__)

class Car_API:


    # Endpoint to show all people.
    @car_api.route("/cars", methods = ["GET"])
    def getCars():
        result = CarModel().getCars()

        return jsonify(result)

    # Endpoint to show all people.
    @car_api.route("/wholecars", methods = ["GET"])
    def getWholeCars():
        result = CarModel().getCarsWithMake()
        return jsonify({'result': [dict(row) for row in result]})