import unittest

from app import app

class AppTestCase(unittest.TestCase):
    def test_x_is_1(self):
        response, status_code = app.cir_sur("1")
        self.assertEqual(response.json, 12.56)
        self.assertEqual(status_code, 200)

    def test_x_is_neg10(self):
        response, status_code = app.cir_sur("-10")
        self.assertEqual(response.json, 0.00)
        self.assertEqual(status_code, 200)

    def test_x_is_1dot5(self):
        response, status_code = app.cir_sur("1.5")
        self.assertEqual(response.json, 28.26)
        self.assertEqual(status_code, 200)

    # def test_true_when_x_is_17(self):
    #     response, status_code = app.is_prime("17")
    #     self.assertEqual(response.json, True)
    #     self.assertEqual(status_code, 200)
        
    # def test_false_when_x_is_36(self):
    #     response, status_code = app.is_prime("36")
    #     self.assertEqual(response.json, False)
    #     self.assertEqual(status_code, 200)
        
    # def test_true_when_x_is_13219(self):
    #     response, status_code = app.is_prime("13219")
    #     self.assertEqual(response.json, True)
    #     self.assertEqual(status_code, 200)
        
    # def test_plus_0_0(self):
    #     response, status_code = app.plus("0", "0")
    #     self.assertEqual(response.json, {"result": 0})
    #     self.assertEqual(status_code, 200)

    # def test_plus_1_0(self):
    #     response, status_code = app.plus("1", "0")
    #     self.assertEqual(response.json, {"result": 1})
    #     self.assertEqual(status_code, 200)

    # def test_plus_0_1(self):
    #     response, status_code = app.plus("0", "2")
    #     self.assertEqual(response.json, {"result": 2})
    #     self.assertEqual(status_code, 200)

    # def test_plus_3_2(self):
    #     response, status_code = app.plus("3", "2")
    #     self.assertEqual(response.json, {"result": 5})
    #     self.assertEqual(status_code, 200)

    # def test_plus_minus_1_0(self):
    #     response, status_code = app.plus("-1", "0")
    #     self.assertEqual(response.json, {"result": -1})
    #     self.assertEqual(status_code, 200)

    # def test_plus_0_minus_1(self):
    #     response, status_code = app.plus("0", "-2")
    #     self.assertEqual(response.json, {"result": -2})
    #     self.assertEqual(status_code, 200)

    # def test_plus_minus_3_minus_5(self):
    #     response, status_code = app.plus("-3", "-5")
    #     self.assertEqual(response.json, {"result": -8})
    #     self.assertEqual(status_code, 200)

    # def test_plus_0_a(self):
    #     response, status_code = app.plus("0", "a")
    #     self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})
    #     self.assertEqual(status_code, 400)

    # def test_plus_a_0(self):
    #     response, status_code = app.plus("a", "0")
    #     self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})
    #     self.assertEqual(status_code, 400)

    # def test_plus_a_a(self):
    #     response, status_code = app.plus("a", "a")
    #     self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})
    #     self.assertEqual(status_code, 400)

if __name__ == "__main__":
    unittest.main()
