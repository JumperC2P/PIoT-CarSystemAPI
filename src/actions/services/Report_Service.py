from datetime import datetime

from .Record_Service import Record_Service
from ..constants.Sys_Constants import car_status
from ..model.Car import Car
from ..model.Car import CarModel
from ..model.Car_Make import Car_Make
from ..model.Car_Make import CarMakeModel
from ..model.Record import RecordModel
from .User_Service import User_Service
from ..model.Report import ReportModel


class Report_Service:
    """Report_Service is a logic layer of report actions."""

    def getReports(self):
        """To get all the report information"""
        reports = ReportModel().find_all_reports()
        return [dict(r) for r in reports]

    def add(self, car_id, admin_id, issue):
        """Add a report data to database"""
        ReportModel().add(car_id, issue, datetime.today(), admin_id)

    def update(self, report_id, car_id, engineer_id):
        """Update the close date and engineer id to report

        Also, update the car status in car table
        """
        ReportModel().update(report_id, datetime.today(), engineer_id)
        CarModel().update_status(car_id, car_status['A'])

    def find_the_new_one(self):
        """Get the lateset report"""
        return ReportModel().getLastReport()
