from flask import Flask, Blueprint, request, jsonify, render_template
from sqlalchemy.exc import ResourceClosedError

from ..model.Record import Record
from ..model.Record import RecordModel
import urllib.parse
from ..utils.parse_qs_plus import ParserUtils
from ..services.User_Service import User_Service
from ..services.Record_Service import Record_Service
import simplejson as json

record_api = Blueprint("record_api", __name__)

class Record_API:

    @record_api.route("/checkRecord", methods=["POST"])
    def checkRecord():
        if request.content_type.startswith("application/json"):
            content = json.loads(request.get_data())
            try:
                users = User_Service().login(content['username'], content['password'])
                user = {'result': [dict(row) for row in users]}
                if len(user['result']) != 0:
                    user = user['result'][0]
                    result = Record_Service().find_records_by_user_id_with_all_return(user['user_id'])
                    return jsonify({'result': result})
            except:
                return jsonify({'result': "Please check your username and password."})

            return jsonify({'result': []})
        else:
            return jsonify({'result': "Wrong Content Type"})