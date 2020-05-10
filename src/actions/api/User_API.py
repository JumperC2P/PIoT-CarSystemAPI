from flask import Flask, Blueprint, request, jsonify, render_template
from ..model.User import User
from ..model.User import UserModel
import json
import urllib.parse
from ..utils.parse_qs_plus import ParserUtils
from ..services.User_Service import User_Service

user_api = Blueprint("user_api", __name__)

class User_API:

    @user_api.route("/user", methods = ["GET"])
    def getUser():
        result = UserModel().getUser()

        return jsonify(result)

    @user_api.route("/login", methods = ["POST"])
    def login():
        if (request.content_type.startswith("application/x-www-form-urlencoded")):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            user = User_Service().login(content['username'], content['password'])
            return jsonify({'result': [dict(row) for row in user]})
        else:
            return "Wrong Content Type"