from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import and_, text
from sqlalchemy.sql import select

db = SQLAlchemy()
ma = Marshmallow()


class Record(db.Model):
    """Record object to store data from database"""
    __tablename__ = "Records"
    record_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    is_return = db.Column(db.Boolean)
    is_cancel = db.Column(db.Boolean)
    est_rent_date = db.Column(db.Date)
    est_return_date = db.Column(db.Date)

    def __init__(self, record_id, car_id, user_id, is_return, est_rent_date, est_return_date, is_cancel):
        self.record_id = record_id
        self.car_id = car_id
        self.user_id = user_id
        self.is_return = is_return
        self.est_rent_date = est_rent_date
        self.est_return_date = est_return_date
        self.is_cancel = is_cancel


class RecordSchema(ma.Schema):
    """Record Schema for database connection"""
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        # Fields to expose.
        fields = ("record_id", "car_id", "user_id", "is_return", "est_rent_date", "est_return_date", "is_cancel")


recordSchema = RecordSchema()
recordsSchema = RecordSchema(many=True)


class RecordModel:
    """RecordModel is used to connect with the Records table in database"""

    def find_records_by_user_id_with_all_return(self, user_id):
        """Query for checking whether the current user has no return cars or booking car.

        :return: a list of records which are booking or rented

        """
        sql = db.text("select record_id, car_id, user_id, is_return, est_rent_date, est_return_date from Records where is_return = 0 and is_cancel = 0 and user_id = :user_id")
        return db.engine.execute(sql, user_id=user_id)

    def find_by_car_id_and_user_id_and_return_and_cancel(self, car_id, user_id, is_return, is_cancel):
        """Query for the booking record of the user

        :return: the booking record of the user

        """
        sql = db.text("select record_id, car_id, user_id, is_return, est_rent_date, est_return_date from Records where car_id = :car_id and user_id = :user_id and is_return = :is_return and is_cancel = :is_cancel")
        return db.engine.execute(sql, car_id=car_id, user_id=user_id, is_return=is_return, is_cancel=is_cancel)

    def find_all(self):
        """Query for the booking record of the user

        :return: the booking record of the user

        """
        sql = select([db.text(
            " c.car_id, c.cost, cm.name as 'make', c.body_type, c.seat_number, c.car_status, c.color, r.record_id, r.user_id, r.est_rent_date, r.est_return_date, r.is_return, r.is_cancel from Cars c, Car_Make cm, Records r "
        )]).where(
            and_(
                text("c.make = cm.id "),
                text("c.car_id = r.car_id ")
            )
        ).order_by(text(" record_id desc"))
        return db.engine.execute(sql)

    def find_newest(self):
        """Query for the latest record

        :return: the latest record object

        """
        sql = db.text("select record_id, car_id, user_id, is_return, est_rent_date, est_return_date from Records order by record_id desc limit 1")
        return db.engine.execute(sql)

    def add(self, car_id, est_rent_date, est_return_date, user_id):
        """add a record
        """
        sql = db.text(
            "Insert into Records (car_id, user_id, est_rent_date, est_return_date) values (:car_id, :user_id, :est_rent_date, :est_return_date)").execution_options(
            autocommit=True)

        result = db.engine.execute(sql,
                                   car_id=car_id, user_id=user_id, est_rent_date=est_rent_date,
                                   est_return_date=est_return_date
                                   )
        return result

    def find_history_by_user_id(self, user_id):
        """Query for the records of user

        :return: a list of records

        """
        sql = select([db.text(
                " c.car_id, c.cost, cm.name as 'make', c.body_type, c.seat_number, c.car_status, c.color, r.record_id, r.user_id, r.est_rent_date, r.est_return_date, r.is_return, r.is_cancel from Cars c, Car_Make cm, Records r "
                )]).where(
                    and_(
                        text("c.make = cm.id "),
                        text("c.car_id = r.car_id "),
                        text("r.user_id = :user_id ")
                    )
                ).order_by(text(" record_id desc"))
        return db.engine.execute(sql, user_id=user_id)

    def update_is_cancel(self, record_id, status):
        """Update the is_cancel flag in record

        """
        sql = text("update Records set is_cancel = :cancel where record_id = :record_id").execution_options(autocommit=True)
        db.engine.execute(sql, cancel=status, record_id=record_id)

    def update_is_return(self, record_id, status):
        """Update the is_return flag in record

        """
        sql = text("update Records set is_return = :is_return where record_id = :record_id").execution_options(autocommit=True)
        db.engine.execute(sql, is_return=status, record_id=record_id)

