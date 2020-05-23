import unittest
import simplejson

from actions.User_Actions import User_Actions
from actions.Car_Actions import Car_Actions
from actions.Record_Actions import Record_Actions


class API_Test(unittest.TestCase):

    def setUp(self):
        self._url = "http://192.168.1.72"
        self._port = "5000"
        self._user = {
            "username": "Test",
            "password": "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f",
            "email": "test@gmail.com",
            "first_name": "Test",
            "last_name": "Test",
            "role": "Customer"
        }

    def tearDown(self):
        pass

    def test_Register(self):
        user = self._user
        user['username'] = "Testing"
        resp = User_Actions().register(self._url, self._port, user)
        self.assertEqual(self._user['username'], resp['result']['username'])

    def test_login(self):
        resp = User_Actions().login(self._url, self._port, "Test", self._user['password'])
        self.assertEqual(1, len(resp['result']))

    def test_show_available_cars(self):
        params = {
            'status': ['Available'],
            'makes': [],
            'colors': [],
            'types': [],
            'seats': []
        }
        resp = Car_Actions().show_available_cars(self._url, self._port, self._user['username'], self._user['password'], params)
        for car in resp['result']:
            self.assertEqual('Available', car['car_status'])

    def test_book(self):
        book_info = {
            'car_id': 14,
            "est_rent_date": '2020-06-12 12:12:12',
            "est_return_date": '2020-06-13 12:12:12'
        }
        resp = Record_Actions().book(self._url, self._port, self._user['username'], self._user['password'], book_info)
        self.assertEqual('0', resp['result']['code'])

    def test_cancel(self):
        record = {
            'record_id': 20,
            'car_id': 15
        }
        resp = Record_Actions().cancel(self._url, self._port, self._user['username'], self._user['password'], record)
        self.assertEqual('0', resp['result']['code'])

    def test_show_history(self):
        resp = Record_Actions().show_history(self._url, self._port, "Frank", self._user['password'])
        for record in resp['result']:
            self.assertEqual(1, record['user_id'])


if __name__ == '__main__':
    unittest.main()
