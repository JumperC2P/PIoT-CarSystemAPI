from flask import Flask, Blueprint, request, jsonify, render_template
from sqlalchemy.exc import ResourceClosedError

from ..constants.Sys_Constants import car_status
from ..utils.google_calendar_utils import Google_Calendar_Utils

from ..model.Record import Record
from ..model.Record import RecordModel
import urllib.parse
from ..utils.parse_qs_plus import ParserUtils
from ..services.User_Service import User_Service
from ..services.Record_Service import Record_Service
from ..services.Car_Service import Car_Service
import simplejson as json

record_api = Blueprint("record_api", __name__)


class Record_API:
    """Record_API organises all the functions which are related to book cars."""

    @record_api.route("/checkRecord", methods=["POST"])
    def checkRecord():
        """Endpoint to check whether the user has booked or rented a car

        :return: If the user can book a new car, return True; otherwise, return False

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    result = Record_Service().find_records_by_user_id_with_all_return(user['user_id'])
                    return jsonify({'result': result})
            except:
                return jsonify({'result': "Please check your username and password."})

            return jsonify({'result': []})
        else:
            return jsonify({'result': "Wrong Content Type"})

    @record_api.route("/getRecords", methods=["POST"])
    def getRecords():
        """Endpoint to get the records of the user

        :return: a list of records of the user

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    if user['role'] == 'Admin':
                        result = Record_Service().find_all()
                    else:
                        result = Record_Service().find_history_by_user_id(user['user_id'])
                    return jsonify({'result': result})
            except:
                return jsonify({'result': "Please check your username and password."})

            return jsonify({'result': []})
        else:
            return jsonify({'result': "Wrong Content Type"})

    @record_api.route("/book", methods=["POST"])
    def book():
        """Endpoint to book a car

        :return: the result of booking operation

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            # try:
            user = User_Service().login(content['username'], content['password'])
            if user:
                try:
                    # check the car
                    car = Car_Service().find_by_car_id(content['book_info']['car_id'])
                    if car:
                        if car['car_status'] != car_status['A']:
                            return jsonify({'result': {'code': '1', 'message': 'The car cannot be booked.'}})
                    else:
                        return jsonify({'result': {'code': '1', 'message': 'Cannot find the car.'}})

                    # book the car
                    record_id = Record_Service().book(content['book_info'], user[
                        'user_id'])  # car_id, est_rent_date, est_return_date, user_id
                    seat = (str(car['seat_number']))

                    # add google calendar event
                    description = "Car ID: {} \nBooked User: {}\nCar Location: {}\nColor: {}\nMake: {}\nBody Type: {}\nSeat Number: {}".format(
                        car['car_id'], content['username'], car['car_location'], car['color'], car['make'],
                        car['body_type'], seat)
                    title = "A Car has been booked - Record ID: {}".format(record_id)

                    Google_Calendar_Utils().insert(title, car['car_location'], description,
                                                   content['book_info']['est_rent_date'],
                                                   content['book_info']['est_return_date'],
                                                   user['email'])

                    return jsonify(
                        {'result': {'code': '0', 'message': 'The car is booked by ' + user['username'] + '.'}})
                except ResourceClosedError:
                    return jsonify({'result': 'error'})
            # except:
            #     return jsonify({'result': "System failed. Please contact with system administrator."})

            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @record_api.route("/cancel_booking", methods=["POST"])
    def cancel_booking():
        """Endpoint to cancel a booking

        :return: the result of canceling a booking

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    record_id = str(content['record']['record_id'])

                    try:
                        # check the car
                        car = Car_Service().find_by_car_id(content['record']['car_id'])
                        if car:
                            if car['car_status'] != car_status['B']:
                                return jsonify({'result': {'code': '1', 'message': 'The car has not been booked.'}})
                        else:
                            return jsonify({'result': {'code': '1', 'message': 'Cannot find the car.'}})

                        # cancel the booking
                        Record_Service().cancel_booking(content['record'])

                        # delete google calendar event
                        Google_Calendar_Utils().delete(str(content['record']['record_id']))

                        return jsonify({'result': {'code': '0', 'message': 'The booking is canceled .'}})
                    except ResourceClosedError:
                        return jsonify({'result': 'error'})
            except:
                return jsonify(
                    {'result': {'code': '2', 'message': "System failed. Please contact with system administrator."}})

            return jsonify({'result': []})
