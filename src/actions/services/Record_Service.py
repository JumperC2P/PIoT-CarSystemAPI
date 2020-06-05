from ..constants.Sys_Constants import car_status
from ..model.Record import RecordModel
from ..model.Car import CarModel
from datetime import datetime


class Record_Service:
    """Record_Service is a logic layer of booking actions."""

    def find_all(self):
        """In the method, it will find the booking history of the current user.

        :return
            all the booking records

        """
        histories = RecordModel().find_all()
        return [dict(h) for h in histories]

    def find_records_by_user_id_with_all_return(self, user_id):
        """In the method, it is used to check whether the current user has no return cars or booking car.

        :param:user_id(int): the user id of current user

        :return
            if there are cars not returned or booked by the user, return False; otherwise, return True

        """
        record = RecordModel().find_records_by_user_id_with_all_return(user_id)
        for r in record:
            return False
        return True

    def find_history_by_user_id(self, user_id):
        """In the method, it will find the booking history of the current user.

        :param: user_id(int): the user id of current user

        :return
            the booking records of the current user

        """
        histories = RecordModel().find_history_by_user_id(user_id)
        return [dict(h) for h in histories]

    def find_by_car_id_and_user_id(self, car_id, user_id):
        """In the method, it will find the booking record of the current user .

        :param: car_id(int): the car id
        :param: user_id(int): the user id of current user

        :return
            the booking record of the current user

        """
        histories = RecordModel().find_by_car_id_and_user_id(car_id, user_id)
        return [dict(h) for h in histories]

    def book(self, book_info, user_id):
        """In the method, it is used to book a car.
        It will add a record and change the status of the booked car.


        :param: book_info(JSON object): the booking information sent from web page
        :param: user_id(int): the user id of the current user

        :return: the record

        """
        # add record
        est_rent_date = datetime.strptime(book_info['est_rent_date'], '%Y-%m-%d %H:%M:%S')
        est_return_date = datetime.strptime(book_info['est_return_date'], '%Y-%m-%d %H:%M:%S')
        RecordModel().add(book_info['car_id'], est_rent_date, est_return_date, user_id)

        # update car status
        CarModel().update_status(book_info['car_id'], car_status['B'])

        record = RecordModel().find_newest()

        for r in record:
            return dict(r)['record_id']
        return None

    def cancel_booking(self, record):
        """In the method, it is used to cancel a car booking, update the status of car and the flag of returning in Records table.

         :param: record(Record object): the record which is going to be canceled.

        """
        car_id = record['car_id']
        record_id = record['record_id']

        # update record
        RecordModel().update_is_cancel(record_id, 1)

        # update car status
        CarModel().update_status(car_id, car_status['A'])

    def find_by_car_id_and_user_id_and_return_and_cancel(self, car_id, user_id, is_return, is_cancel):
        records = RecordModel().find_by_car_id_and_user_id_and_return_and_cancel(car_id, user_id, 0, 0)
        for r in records:
            return dict(r)
        return None
