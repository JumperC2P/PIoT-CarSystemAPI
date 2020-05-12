from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Record(db.Model):
    __tablename__ = "Records"
    record_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    is_return = db.Column(db.Boolean)
    est_rent_date = db.Column(db.Date)
    est_return_date = db.Column(db.Date)

    def __init__(self, record_id, car_id, user_id, is_return, est_rent_date, est_return_date):
        self.record_id = record_id
        self.car_id = car_id
        self.user_id = user_id
        self.is_return = is_return
        self.est_rent_date = est_rent_date
        self.est_return_date = est_return_date


class RecordSchema(ma.Schema):
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        # Fields to expose.
        fields = ("record_id", "car_id", "user_id", "is_return", "est_rent_date", "est_return_date")


recordSchema = RecordSchema()
recordsSchema = RecordSchema(many=True)


class RecordModel:

    def find_records_by_user_id_with_all_return(self, user_id):
        sql = db.text("select record_id, car_id, user_id, is_return, est_rent_date, est_return_date from Records where is_return = 0 and user_id = :user_id")
        return db.engine.execute(sql, user_id=user_id)

    def add(self, car_id, est_rent_date, est_return_date, user_id):
        sql = db.text(
            "Insert into Records (car_id, user_id, est_rent_date, est_return_date) values (:car_id, :user_id, :est_rent_date, :est_return_date)").execution_options(
            autocommit=True)

        result = db.engine.execute(sql,
                                   car_id=car_id, user_id=user_id, est_rent_date=est_rent_date,
                                   est_return_date=est_return_date
                                   )
        return result
