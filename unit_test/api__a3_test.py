import unittest
import simplejson

from actions.User_Actions import User_Actions
from actions.Car_Actions import Car_Actions
from actions.Record_Actions import Record_Actions


class API_Test(unittest.TestCase):

    def setUp(self):
        # self._url = "http://192.168.1.72"
        self._url = "http://127.0.0.1"
        self._port = "5000"
        self._admin = {
            "username": "Frank",
            "password": "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f",
        }
        self._engineer = {
            "username": "Zoe",
            "password": "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f",
        }
        self._update_car = {
            "car_id": 15,
            "cost": 33.2,
            "make": 9,
            "body_type": "T6",
            "seat_number": 15,
            "car_location": "-37.818408,144.963706",
            "color": "silver"
        }
        self._update_user = {
            "user_id": 21,
            "first_name": "UnitTest",
            "last_name": "UnitTest",
            "email": "unittest@gmail.com"
        }
        self._remove_car = 16
        self._remove_user = 21
        self._report = {
            "car_id": 15,
            "issue": "UnitTest",
            "admin_id": 1
        }
        self._close_report = {
            "report_id": 14,
            "car_id": 2,
            "engineer_id": 4
        }

    def tearDown(self):
        pass

    def test_update_car(self):
        resp = Car_Actions().update_car(self._url, self._port, self._admin['username'], self._admin['password'],
                                        self._update_car)
        self.assertEqual(True, resp['result'])

    def test_remove_car(self):
        resp = Car_Actions().remove_car(self._url, self._port, self._admin['username'], self._admin['password'],
                                        self._remove_car)
        self.assertEqual(True, resp['result'])

    def test_show_rental_history(self):
        resp = Record_Actions().show_history(self._url, self._port, self._admin['username'], self._admin['password'])
        self.assertNotEqual(0, len(resp['result']))

    def test_update_user(self):
        resp = User_Actions().update_user(self._url, self._port, self._admin['username'], self._admin['password'], self._update_user)
        self.assertEqual('UnitTest', resp['result']['first_name'])

    def test_remove_user(self):
        resp = User_Actions().remove_user(self._url, self._port, self._admin['username'], self._admin['password'], self._remove_user)
        self.assertEqual(True, resp['result'])

    def test_report_car(self):
        resp = Car_Actions().report_car(self._url, self._port, self._admin['username'], self._admin['password'], self._report)
        self.assertEqual(True, resp['result'])

    def test_close_report(self):
        resp = Car_Actions().close_report(self._url, self._port, self._admin['username'], self._admin['password'], self._close_report)
        self.assertEqual(True, resp['result'])


if __name__ == '__main__':
    unittest.main()
