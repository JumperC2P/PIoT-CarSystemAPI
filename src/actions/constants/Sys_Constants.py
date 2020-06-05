"""Sys_Constants contains some constants used in the application."""

car_status = dict()
car_status['A'] = "Available"
car_status['B'] = "Booked"
car_status['R'] = "Rented"
car_status['P'] = "Reported"

rent_status = dict()
rent_status[None] = "Booked"
rent_status[0] = "Rented"
rent_status[1] = "Returned"
