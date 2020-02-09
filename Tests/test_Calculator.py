import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        self.assertEqual(3, self.calculator.Sum(1, 2))

    def test_calculator_result_access_difference_result(self):
        self.calculator.Difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_result_access_Sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_multiple_result_calculator(self):
        calculator1 = Calculator()
        calculator2 = Calculator()

        calculator1.Sum(1, 2)
        calculator2.Difference(3, 4)
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)

    def test_product_result_calculator(self):
        self.calculator.Product(2, 4)
        self.assertEqual(8, self.calculator.Result)

    def test_division_result_calculator(self):
        self.calculator.Fraction(6, 3)
        self.assertEqual(2, self.calculator.Result)

    def test_power_result_calculator(self):
        self.calculator.Power(2, 3)
        self.assertEqual(8, self.calculator.Result)

    def test_root_result_calculator(self):
        self.calculator.Root(2, 16)
        self.assertEqual(4, self.calculator.Result)

    def test_log_result_calculator(self):
        float(self.calculator.Log(2, 4))
        self.assertEqual(2, self.calculator.Result)


if __name__ == '__main__':
    unittest.main()
