from flask import Flask, Blueprint, request, jsonify, render_template
from sqlalchemy import text, and_
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ..db_connection.DBConnection import DBConnection
from sqlalchemy.sql import select

db = DBConnection().db
ma = DBConnection().ma


class User(db.Model):
    """User object to store data from database"""
    __tablename__ = "Users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    email = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    role = db.Column(db.Text)
    mac_address = db.Column(db.Text)

    def __init__(self, user_id, username, password, email, first_name, last_name, role, mac_address):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.last_name = last_name
        self.first_name = first_name
        self.role = role
        self.mac_address = mac_address


class UserSchema(ma.Schema):
    """User Schema for database connection"""

    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        # Fields to expose.
        fields = ("user_id", "username", "password", "email", "first_name", "last_name", "role", "mac_address")


userSchema = UserSchema()
usersSchema = UserSchema(many=True)


class UserModel:
    """UserModel is used to connect with the Records table in database"""

    def getUser(self):
        """Query for all user information

        :return: a list of users

        """
        user = User.query.all()
        result = usersSchema.dump(user)

        return result

    def login(self, username, password):
        """Query for all user information

        :return: a list of users

        """
        user = db.engine.execute(text("select * from Users where username= :username and password = :password").
                                 bindparams(username=username).bindparams(password=password))
        return user

    def checkUserName(self, username):
        """Query for the indicated username

        :return: the user object

        """
        user = db.engine.execute(text("select * from Users where username= :username").
                                 bindparams(username=username))
        return user

    def getLastUserId(self):
        """Find the latest user id

        :return: the latest user id

        """
        users = db.engine.execute(text("select * from Users order by user_id desc limit 1"))
        for user in users:
            return user.user_id

    def add(self, user_id, username, password, first_name, last_name, email, role):
        """add a user

        :return: the user object

        """
        newUser = User(user_id=user_id, username=username, password=password, first_name=first_name,
                       last_name=last_name, email=email, role=role)

        db.session.add(newUser)
        db.session.commit()

        return newUser

    def update(self, user_id, first_name, last_name, email):
        """update a user
        """
        sql = text(
            "update Users set first_name = :first_name, last_name = :last_name, email=:email where user_id = :user_id").execution_options(
            autocommit=True)
        db.engine.execute(sql, first_name=first_name, last_name=last_name, email=email, user_id=user_id)

    def updatePassword(self, new_password, user_id):
        """update user's password
        """
        sql = text(
            "update Users set password = :new_password where user_id = :user_id").execution_options(
            autocommit=True)
        db.engine.execute(sql, new_password=new_password, user_id=user_id)

    def getUsersWithparams(self, params):
        """Find users' information with indicated conditions

        :return: a list of users

        """
        sql = select([text(
            " user_id, username, email, password, first_name, last_name, role from Users ")]) \
            .where(
            and_(
                text("username like :username" if len(params['username']) != 0 else "1=:username"),
                text("email like :email" if len(params['email']) != 0 else "1=:email"),
                text("first_name like :first_name" if len(params['first_name']) != 0 else "1=:first_name"),
                text("last_name like :last_name" if len(params['last_name']) != 0 else "1=:last_name"),
                text("role in :role" if len(params['role']) != 0 else "1=:role")
            )
        )
        result = db.engine.execute(sql,
                                   username=params['username'] if len(params['username']) != 0 else "1",
                                   email=params['email'] if len(params['email']) != 0 else "1",
                                   first_name=params['first_name'] if len(params['first_name']) != 0 else "1",
                                   last_name=params['last_name'] if len(params['last_name']) != 0 else "1",
                                   role=params['role'] if len(params['role']) != 0 else "1"
                                   )
        return result

    def deleteUser(self, user_id):
        """delete user
        """
        sql = text("delete from Users where user_id = :user_id").execution_options(autocommit=True)
        db.engine.execute(sql, user_id=user_id)

    def find_by_mac_address(self, mac_address):
        """Find user by Mac address
        """
        users = db.engine.execute(text("select * from Users where mac_address= :mac_address").
                                  bindparams(mac_address=mac_address))
        for u in users:
            return dict(u)
        return None

    def find_by_user_id(self, user_id):
        """Find user by user id
        """
        users = db.engine.execute(text("select * from Users where user_id= :user_id").
                                  bindparams(user_id=user_id))
        for u in users:
            return dict(u)
        return None
