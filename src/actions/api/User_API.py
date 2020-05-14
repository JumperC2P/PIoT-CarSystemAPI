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
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                user = User_Service().login(content['username'], content['password'])
                if user:
                    user['password'] = content['password']
                    print(user)
                    user = {'result': [user]}
                    user = jsonify(user)
                    return user
            except:
                return "Please check your username and password."
            
            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @user_api.route("/register", methods = ["POST"])
    def register():
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                user = User_Service().register(content['username'], content['password'], content['first_name'], content['last_name'], content['email'], content['role'])
                if user:
                    new_user = dict()
                    new_user['user_id'] = user.user_id
                    new_user['username'] = user.username
                    new_user['password'] = content['password']
                    new_user['first_name'] = user.first_name
                    new_user['last_name'] = user.last_name
                    new_user['email'] = user.email
                    new_user['role'] = user.role
                    user = jsonify({'result': new_user})
                    return user
            except:
                return "Please check your information."
            
            return jsonify({'result': []})
        else:
            return "Wrong Content Type"

    @user_api.route("/checkUserName", methods = ["POST"])
    def checkUserName():
        if request.content_type.startswith("application/x-www-form-urlencoded"):
            content = ParserUtils().parse_qs_plus(urllib.parse.parse_qs(request.get_data().decode("utf-8")))
            try:
                result = User_Service().checkUserName(content['username'])
                result = jsonify({'result': result})
                return result
            except:
                return "Please check your information."
            
            return jsonify({'result': []})
        else:
            return "Wrong Content Type"