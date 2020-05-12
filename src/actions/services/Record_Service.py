from ..model.Record import RecordModel

class Record_Service:

    def find_records_by_user_id_with_all_return(self, user_id):
        record = RecordModel().find_records_by_user_id_with_all_return(user_id)
        for r in record:
            return False
        return True


