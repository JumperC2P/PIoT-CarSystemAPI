from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class DBConnection:

    db = SQLAlchemy()
    ma = Marshmallow()