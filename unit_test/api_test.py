import unittest


class API_Test(unittest.TestCase):

    def setUp(self):
        self._url = "http://127.0.0.1"
        self._port = "5000"
        self._username = "Test"
        self._password = "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"

    def tearDown(self):
        pass

    def test_login_Success(self):


    def test_login_Fail(self):



if __name__ == '__main__':
    unittest.main()
