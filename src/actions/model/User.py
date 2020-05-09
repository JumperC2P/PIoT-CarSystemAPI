from flask import Flask, Blueprint, request, jsonify, render_template
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


    

