from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Record(db.Model):
    __tablename__ = "Records"
    record_id = db.Column(db.Integer, primary_key = True)
    car_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    def __init__(self, record_id, car_id, user_id):
        self.record_id = record_id
        self.car_id = car_id
        self.user_id = user_id


class RoleSchema(ma.Schema):
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("record_id", "car_id", "user_id")