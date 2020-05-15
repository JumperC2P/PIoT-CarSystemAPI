from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, and_
from flask_marshmallow import Marshmallow
from ..db_connection.DBConnection import DBConnection
from sqlalchemy.sql import select

db = DBConnection().db
ma = DBConnection().ma


class Car(db.Model):
    """Car object to store data from database"""

    __tablename__ = "Cars"
    car_id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Numeric)
    make = db.Column(db.Text)
    body_type = db.Column(db.Text)
    seat_number = db.Column(db.Integer)
    car_status = db.Column(db.Text)
    car_location = db.Column(db.Text)
    color = db.Column(db.Text)

    def __init__(self, car_id, cost, make, body_type, seat_number, car_status, car_location, color):
        self.car_id = car_id
        self.cost = cost
        self.make = make
        self.body_type = body_type
        self.seat_number = seat_number
        self.car_status = car_status
        self.car_location = car_location
        self.color = color


class CarSchema(ma.Schema):
    """Car Schema for database connection"""

    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        # Fields to expose.
        fields = ("car_id", "cost", "make", "body_type", "seat_number", "car_status", "car_location", "color")


carSchema = CarSchema()
carsSchema = CarSchema(many=True)


class CarModel:
    """CarModel is used to connect with the Cars table in database"""

    def getCars(self):
        """Query for all cars information

        :return: a list of cars

        """
        cars = Car.query.all()
        return carsSchema.dump(cars)

    def getCarsWithMake(self):
        """Query for all cars information with manufacturer name

        :return: a list of cars

        """
        result = db.engine.execute(text(
            "select c.car_id, c.cost, cm.name as 'make', c.body_type, c.seat_number, c.car_status, c.car_location, c.color "
            + "from Cars c, Car_Make cm "
            + "where c.make = cm.id "))  # text().execution_options(autocommit=True)
        return result

    def getSeatNumbers(self):
        """Query for all the seat numbers

        :return: a list of seat number

        """
        result = db.engine.execute(text("select distinct seat_number from Cars order by seat_number asc"))
        return result

    def getBodyTypes(self):
        """Query for all the body types

        :return: a list of body types

        """
        result = db.engine.execute(text("select distinct body_type from Cars order by body_type asc"))
        return result

    def getColors(self):
        """Query for all the colors

        :return: a list of colors

        """
        result = db.engine.execute(text("select distinct color from Cars order by color asc"))
        return result

    def find_by_car_id(self, car_id):
        """Find the car information with indicated car id

        :return: a Car object

        """
        sql = select([text(
            " c.car_id, c.cost, cm.name as 'make', c.body_type, c.seat_number, c.car_status, c.car_location, c.color from Cars c, Car_Make cm ")]) \
            .where(and_(text("c.make = cm.id "), text("c.car_id = :car_id")))
        result = db.engine.execute(sql, car_id=car_id)
        return result

    def update_status(self, car_id, status):
        """Update status of car
        """
        sql = text("update Cars set car_status = :status where car_id = :car_id").execution_options(autocommit=True)
        db.engine.execute(sql, status=status, car_id=car_id)

    def getCarsWithparams(self, params):
        """Find cars information with indicated conditions

        :return: a list of cars

        """
        sql = select([text(
            " c.car_id, c.cost, cm.name as 'make', c.body_type, c.seat_number, c.car_status, c.car_location, c.color from Cars c, Car_Make cm ")]) \
            .where(
            and_(
                text("c.make = cm.id "),
                text("cm.name in :make" if len(params['makes']) != 0 else "1=:make"),
                text("c.color in :color" if len(params['colors']) != 0 else "1=:color"),
                text("c.body_type in :type" if len(params['types']) != 0 else "1=:type"),
                text("c.seat_number in :seat" if len(params['seats']) != 0 else "1=:seat")
            )
        )

        result = db.engine.execute(sql,
                                   make=params['makes'] if len(params['makes']) != 0 else "1",
                                   color=params['colors'] if len(params['colors']) != 0 else "1",
                                   type=params['types'] if len(params['types']) != 0 else "1",
                                   seat=params['seats'] if len(params['seats']) != 0 else "1"
                                   )
        return result
