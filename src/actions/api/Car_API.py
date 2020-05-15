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

    # Endpoint to show all people.
    # Endpoint to show all people.
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
                    print([dict(row) for row in result])
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


