from flask import Flask, Blueprint, request, jsonify, render_template
from ..model.Car import Car
from ..model.Car import CarModel
import urllib.parse
from ..utils.parse_qs_plus import ParserUtils
from ..services.User_Service import User_Service

car_api = Blueprint("car_api", __name__)

class Car_API:


    # Endpoint to show all people.
    @car_api.route("/cars", methods = ["GET"])
    def getCars():
        result = CarModel().getCars()

        return jsonify(result)

    # Endpoint to show all people.
    @car_api.route("/getAllCars", methods = ["POST"])
    def getWholeCars():

        if (request.content_type.startswith("application/x-www-form-urlencoded")):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                users = User_Service().login(content['username'], content['password'])
                user = {'result': [dict(row) for row in users]}
                if (len(user['result']) != 0):
                    result = CarModel().getCarsWithMake()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."
            
            return jsonify({'result': []})
        else:
            return "Wrong Content Type"


        