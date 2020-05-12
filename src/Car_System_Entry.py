from flask import Flask;
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from actions.api.User_API import user_api
from actions.api.CarMake_API import car_make_api
from actions.api.Car_API import car_api
from actions.api.Record_API import record_api
from actions.db_connection.DBConnection import DBConnection
import pymysql
from flask_cors import CORS

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


class Car_System_Entry:
    db = DBConnection().db

    # Update HOST and PASSWORD appropriately.
    HOST = "127.0.0.1"
    USER = "root"
    PASSWORD = "Pa55W0rd"
    DATABASE = "piot"

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    db.init_app(app)

    app.register_blueprint(user_api)
    app.register_blueprint(car_make_api)
    app.register_blueprint(car_api)
    app.register_blueprint(record_api)


if __name__ == '__main__':
    app.run()
