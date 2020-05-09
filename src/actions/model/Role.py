from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Role(db.Model):
    __tablename__ = "Roles"
    role_id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.Text)

    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name


class RoleSchema(ma.Schema):
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("role_id", "role_name")