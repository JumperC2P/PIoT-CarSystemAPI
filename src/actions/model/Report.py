from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import and_, text
from sqlalchemy.sql import select

db = SQLAlchemy()
ma = Marshmallow()


class Report(db.Model):
    """Report object to store data from database"""
    __tablename__ = "Records"
    report_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer)
    issue = db.Column(db.String)
    report_date = db.Column(db.Date)
    close_date = db.Column(db.Date)
    admin_id = db.Column(db.Integer)
    engineer_id = db.Column(db.Integer)

    def __init__(self, report_id, car_id, issue, report_date, close_date, admin_id, engineer_id):
        self.report_id = report_id
        self.car_id = car_id
        self.issue = issue
        self.report_date = report_date
        self.close_date = close_date
        self.admin_id = admin_id
        self.engineer_id = engineer_id


class ReportSchema(ma.Schema):
    """Report Schema for database connection"""

    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        # Fields to expose.
        fields = ("report_id", "car_id", "issue", "report_date", "close_date", "admin_id", "engineer_id")


reportSchema = ReportSchema()
reportsSchema = ReportSchema(many=True)


class ReportModel:
    """ReportModel is used to connect with the Reports table in database"""

    def find_all_reports(self):
        """Query for all reports.

        :return: a list of reports

        """
        sql = db.text("select r.report_id, c.car_id, r.issue, r.report_date, r.close_date, r.admin_id, r.engineer_id, c.car_location from Reports r, Cars c where r.car_id = c.car_id order by r.report_id desc")
        return db.engine.execute(sql)

    def add(self, car_id, issue, report_date, admin_id):
        """add a record
        """
        sql = db.text(
            "Insert into Reports (car_id, issue, report_date, admin_id) values (:car_id, :issue, :report_date, :admin_id)").execution_options(
            autocommit=True)

        db.engine.execute(sql,
                          car_id=car_id, issue=issue, report_date=report_date,
                          admin_id=admin_id
                          )

    def update(self, report_id, close_date, engineer_id):
        """update a report
        """
        sql = db.text(
            "update Reports set close_date = :close_date, engineer_id = :engineer_id where report_id = :report_id").execution_options(
            autocommit=True)

        db.engine.execute(sql,
                          close_date=close_date, engineer_id=engineer_id, report_id=report_id
                          )

    def getLastReport(self):
        """Find the latest report

        :return: the latest report with car information

        """
        reports = db.engine.execute(text("select p.report_id, c.car_id, m.name, c.body_type, c.car_location from Reports p, Cars c, Car_Make m where p.car_id = c.car_id and m.id = c.make order by p.report_id desc limit 1"))
        for report in reports:
            return report
