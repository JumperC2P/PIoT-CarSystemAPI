from flask import Flask, Blueprint, request, jsonify, render_template
from sqlalchemy.exc import ResourceClosedError

from ..constants.Sys_Constants import car_status
from ..utils.google_calendar_utils import Google_Calendar_Utils

from ..model.Record import Record
from ..model.Record import RecordModel
import urllib.parse
from ..utils.parse_qs_plus import ParserUtils
from ..services.User_Service import User_Service
from ..services.Report_Service import Report_Service
from ..services.Car_Service import Car_Service
import simplejson as json

report_api = Blueprint("report_api", __name__)


class Report_API:
    """Report_API organises all the functions which are related to report cars."""

    @report_api.route("/getReports", methods=["POST"])
    def getReports():
        """Endpoint to get the reports

        :return: a list of reports

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    result = Report_Service().getReports()
                    return jsonify({'result': result})
            except:
                return jsonify({'result': "Please check your username and password."})

            return jsonify({'result': []})
        else:
            return jsonify({'result': "Wrong Content Type"})

    @report_api.route("/closeReport", methods=["POST"])
    def closeReport():
        """Endpoint to close the reports

        :return: true: success

        """
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            # try:
            user = User_Service().login(content['username'], content['password'])
            if user:
                Report_Service().update(content['report_id'], content['car_id'], content['engineer_id'])
                return jsonify({'result': True})
            # except:
            #     return jsonify({'result': "Please check your username and password."})

            return jsonify({'result': []})
        else:
            return jsonify({'result': "Wrong Content Type"})
