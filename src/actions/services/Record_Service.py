from ..constants.Sys_Constants import car_status
from ..model.Record import RecordModel
from ..model.Car import CarModel

class Record_Service:

    def find_records_by_user_id_with_all_return(self, user_id):
        record = RecordModel().find_records_by_user_id_with_all_return(user_id)
        for r in record:
            return False
        return True

    def find_history_by_user_id(self, user_id):
        histories = RecordModel().find_history_by_user_id(user_id)
        return [dict(h) for h in histories]

    def cancel_booking(self, record):
        car_id = record['car_id']
        record_id = record['record_id']

        # update record
        RecordModel().update_is_cancel(record_id, 1)

        # update car status
        CarModel().update_status(car_id, car_status['A'])


