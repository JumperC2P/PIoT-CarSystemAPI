from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class DBConnection:
    """DBConnection is to create database connection."""

    db = SQLAlchemy()
    ma = Marshmallow()