from flask import Flask, Blueprint, request, jsonify, render_template
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ..db_connection.DBConnection import DBConnection

db = DBConnection().db
ma = DBConnection().ma

class User(db.Model):
    __tablename__ = "Users"
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    email = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    role = db.Column(db.Text)

    def __init__(self, user_id, username, password, email, first_name, last_name, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.last_name = last_name
        self.first_name = first_name
        self.role = role


class UserSchema(ma.Schema):
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("user_id", "username", "password", "email", "first_name", "last_name", "role")

userSchema = UserSchema()
usersSchema = UserSchema(many = True)

class UserModel:

    def getUser(self):
        user = User.query.all()
        result = usersSchema.dump(user)

        return result

    def login(self, username, password):
        user = db.engine.execute(text("select * from Users where username= :username and password = :password").
                                bindparams(username = username).bindparams(password = password))
        return user

    def checkUserName(self, username):
        user = db.engine.execute(text("select * from Users where username= :username").
                                bindparams(username = username))
        return user

    def getLastUserId(self):
        users = db.engine.execute(text("select * from Users order by user_id desc limit 1"))
        for user in users:
            return user.user_id

    def add(self, user_id, username, password, first_name, last_name, email, role):

        newUser = User(user_id = user_id, username = username, password = password, first_name=first_name, last_name=last_name, email=email, role = role)

        db.session.add(newUser)
        db.session.commit()

        return newUser
