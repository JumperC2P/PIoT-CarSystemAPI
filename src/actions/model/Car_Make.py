from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Car_Make(db.Model):
    """Car Make object to store data from database"""
    __tablename__ = "Car_Make"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class CarMakeSchema(ma.Schema):
    """Car Make Schema for database connection"""

    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        # Fields to expose.
        fields = ("id", "name")


carMakeSchema = CarMakeSchema()
carMakesSchema = CarMakeSchema(many=True)


class CarMakeModel:
    """CarMakeModel is used to connect with the CarMakes table in database"""

    def getCarMakes(self):
        """Query for all cars makes
        :return: a list of cars
        """
        carMakes = Car_Make.query.all()
        return carMakesSchema.dump(carMakes)
