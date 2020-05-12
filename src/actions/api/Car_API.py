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

    # Endpoint to show all people.
    @car_api.route("/getAllCars", methods=["POST"])
    def getWholeCars():

        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                users = User_Service().login(content['username'], content['password'])
                user = {'result': [dict(row) for row in users]}
                if len(user['result']) != 0:
                    result = Car_Service().getCarsWithMake()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getMakes", methods=["POST"])
    def getMakes():
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                users = User_Service().login(content['username'], content['password'])
                user = {'result': [dict(row) for row in users]}
                if len(user['result']) != 0:
                    result = Car_Service().getMakes()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getSeatNumbers", methods=["POST"])
    def getSeatNumbers():
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                users = User_Service().login(content['username'], content['password'])
                user = {'result': [dict(row) for row in users]}
                if len(user['result']) != 0:
                    result = Car_Service().getSeatNumbers()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getBodyTypes", methods=["POST"])
    def getBodyTypes():
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                users = User_Service().login(content['username'], content['password'])
                user = {'result': [dict(row) for row in users]}
                if len(user['result']) != 0:
                    result = Car_Service().getBodyTypes()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getColors", methods=["POST"])
    def getColors():
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                users = User_Service().login(content['username'], content['password'])
                user = {'result': [dict(row) for row in users]}
                if len(user['result']) != 0:
                    result = Car_Service().getColors()
                    return jsonify({'result': [dict(row) for row in result]})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/getCarsWithparams", methods=["POST"])
    def getCarsWithparams():
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            # try:
            users = User_Service().login(content['username'], content['password'])
            user = {'result': [dict(row) for row in users]}
            if (len(user['result']) != 0):
                result = Car_Service().getCarsWithparams(content['params'])
                return jsonify({'result': [dict(row) for row in result]})
            # except:
            # return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @car_api.route("/book", methods=["POST"])
    def book():
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            try:
                users = User_Service().login(content['username'], content['password'])
                user = {'result': [dict(row) for row in users]}
                if len(user['result']) != 0:
                    try:
                        # check the car
                        car = Car_Service().find_by_car_id(content['book_info']['car_id'])
                        if car:
                            if car['car_status'] != 'Available':
                                return jsonify({'result': {'code': '1', 'message': 'The car cannot be booked.'}})
                        else:
                            return jsonify({'result': {'code': '1', 'message': 'Cannot find the car.'}})

                        # book the car
                        Car_Service().book(content['book_info'], user['result'][0][
                            'user_id'])  # car_id, est_rent_date, est_return_date, user_id
                        return jsonify({'result': { 'code': '0', 'message': 'The car is booked by ' + user['result'][0]['username'] + '.'}})
                    except ResourceClosedError:
                        return jsonify({'result': 'error'})
            except:
                return "Please check your username and password."

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"
