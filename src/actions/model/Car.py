from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ..db_connection.DBConnection import DBConnection

db = DBConnection().db
ma = DBConnection().ma

class Car(db.Model):
    __tablename__ = "Cars"
    car_id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.Integer)
    make = db.Column(db.Integer)
    body_type = db.Column(db.Text)
    seat_number = db.Column(db.Integer)
    car_status = db.Column(db.Text)
    car_location = db.Column(db.Text)

    def __init__(self, car_id, year, make, body_type, seat_number, car_status, car_location):
        self.car_id = car_id
        self.year = year
        self.make = make
        self.body_type = body_type
        self.seat_number = seat_number
        self.car_status = car_status
        self.car_location = car_location


class CarrSchema(ma.Schema):
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("car_id", "year", "make", "body_type", "seat_number", "car_status", "car_location")


    

