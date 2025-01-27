import unittest

from app import app

class AppTestCase(unittest.TestCase):

    def test_plus_0_0(self):
        response, status_code = app.plus("0", "0")
        self.assertEqual(response.json, {"result": 0})
        self.assertEqual(status_code, 200)

    def test_plus_1_0(self):
        response, status_code = app.plus("1", "0")
        self.assertEqual(response.json, {"result": 1})
        self.assertEqual(status_code, 200)

    def test_plus_0_1(self):
        response, status_code = app.plus("0", "2")
        self.assertEqual(response.json, {"result": 2})
        self.assertEqual(status_code, 200)

    def test_plus_3_2(self):
        response, status_code = app.plus("3", "2")
        self.assertEqual(response.json, {"result": 5})
        self.assertEqual(status_code, 200)

    def test_plus_minus_1_0(self):
        response, status_code = app.plus("-1", "0")
        self.assertEqual(response.json, {"result": -1})
        self.assertEqual(status_code, 200)

    def test_plus_0_minus_1(self):
        response, status_code = app.plus("0", "-2")
        self.assertEqual(response.json, {"result": -2})
        self.assertEqual(status_code, 200)

    def test_plus_minus_3_minus_5(self):
        response, status_code = app.plus("-3", "-5")
        self.assertEqual(response.json, {"result": -8})
        self.assertEqual(status_code, 200)

    def test_plus_0_a(self):
        response, status_code = app.plus("0", "a")
        self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})
        self.assertEqual(status_code, 400)

    def test_plus_a_0(self):
        response, status_code = app.plus("a", "0")
        self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})
        self.assertEqual(status_code, 400)

    def test_plus_a_a(self):
        response, status_code = app.plus("a", "a")
        self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})
        self.assertEqual(status_code, 400)

if __name__ == "__main__":
    unittest.main()
