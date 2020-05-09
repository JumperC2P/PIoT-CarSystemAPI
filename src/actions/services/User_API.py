from flask import Flask, Blueprint, request, jsonify, render_template
from ..model.User import User
from ..model.User import UserSchema

user_api = Blueprint("user_api", __name__)

userSchema = UserSchema()
usersSchema = UserSchema(many = True)

class User_API:


    # Endpoint to show all people.
    @user_api.route("/user", methods = ["GET"])
    def getUser():
        user = User.query.all()
        result = usersSchema.dump(user)

        return jsonify(result)