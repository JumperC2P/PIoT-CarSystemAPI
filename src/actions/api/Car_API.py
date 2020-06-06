from flask import Flask, Blueprint, request, jsonify, render_template
from sqlalchemy.exc import ResourceClosedError

from ..model.Car import Car
from ..model.Car import CarModel
import urllib.parse

from ..utils.parse_qs_plus import ParserUtils
from ..services.User_Service import User_Service
from ..services.Car_Service import Car_Service
import simplejson as json

car_api = Blueprint("car_api", __name__)


class Car_API:
    """Car_API is the entry point of car actions."""

    @car_api.route("/getAllCars", methods=["POST"])
    def getWholeCars():
        """Endpoint to get all car details.

        :return: a list of all the car details

        """
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    result = Car_Service().getCarsWithMake()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getMakes", methods=["POST"])
    def getMakes():
        """Endpoint to get all car manufacturer.

        :return: a list of manufacturer

        """
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    result = Car_Service().getMakes()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getSeatNumbers", methods=["POST"])
    def getSeatNumbers():
        """Endpoint to get all seat numbers.

        :return: a list of seat numbers

        """
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    result = Car_Service().getSeatNumbers()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getBodyTypes", methods=["POST"])
    def getBodyTypes():
        """Endpoint to get all the body types of cars.

        :return: a list of body types of cars

        """
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    result = Car_Service().getBodyTypes()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getColors", methods=["POST"])
    def getColors():
        """Endpoint to get all the color of cars.

        :return: a list of color of cars

        """
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    result = Car_Service().getColors()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getCarsWithparams", methods=["POST"])
    def getCarsWithparams():
        """Endpoint to get car details with indicated conditions

        :return: a list of cars with indicated conditions

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            # try:
            user = User_Service().login(content['username'], content['password'])
            if user:
                result = Car_Service().getCarsWithparams(content['params'])
                return jsonify({'result': [dict(row) for row in result]})
            # except:
            # return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/addCar", methods=["POST"])
    def addCar():
        """Endpoint to add car

        :return: true if successfully

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            # try:
            user = User_Service().login(content['username'], content['password'])
            if user:
                result = Car_Service().addCar(content['car'])
                if result:
                    return jsonify({'result': True})
                else:
                    return jsonify({'result': False})

            # except:
            #     return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/removeCar", methods=["POST"])
    def removeCar():
        """Endpoint to remove car

        :return: true if successfully

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    Car_Service().removeCar(content['car_id'])
                    return jsonify({'result': True})
                else:
                    return jsonify({'result': False})

            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/reportCar", methods=["POST"])
    def reportCar():
        """Endpoint to remove car

        :return: true if successfully

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            # try:
            user = User_Service().login(content['username'], content['password'])
            if user:
                Car_Service().reportCar(content['car_id'], content['admin_id'], content['issue'])
                return jsonify({'result': True})
            else:
                return jsonify({'result': False})

            # except:
            #     return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/pushtest", methods=["POST"])
    def pushtest():
        """Endpoint to remove car

        :return: true if successfully

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            # try:
            user = User_Service().login(content['username'], content['password'])
            if user:
                Car_Service().send_pushbullet_with_report_info()
                return jsonify({'result': True})
            else:
                return jsonify({'result': False})

            # except:
            #     return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/updateCar", methods=["POST"])
    def updateCar():
        """Endpoint to add car

        :return: true if successfully

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    Car_Service().updateCar(content['car'])
                    return jsonify({'result': True})

            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"
