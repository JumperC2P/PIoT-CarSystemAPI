from flask import Flask;
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from actions.api.User_API import user_api
from actions.api.Car_API import car_api
from actions.api.Record_API import record_api
from actions.db_connection.DBConnection import DBConnection
import pymysql
from flask_cors import CORS

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


# coding=UTF-8
class Car_System_Entry:
    """Car_System_Entry.py is the start point of the application"""

    # create a database connection
    db = DBConnection().db

    # Update HOST and PASSWORD appropriately.
    HOST = "35.189.29.28"
    # HOST = "127.0.0.1"
    USER = "root"
    PASSWORD = "Pa55W0rd"
    DATABASE = "piot"

    # database connection setting
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    # initiate the application
    db.init_app(app)

    # register all the api object to the application
    app.register_blueprint(user_api)
    app.register_blueprint(car_api)
    app.register_blueprint(record_api)


if __name__ == '__main__':
    app.run()
