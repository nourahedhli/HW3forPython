import unittest

from MathOperations.additon import Addition
from MathOperations.subtraction import Subtraction

class MyTestCase(unittest.TestCase):



    def test_MathOperation_addition(self):
        self.assertEqual(3, Addition.sum(1,2))


    def test_MathOperation_subtraction(self):

        self.assertEqual(-1, Subtraction.difference(1,2))


    def test_MathOperation_sum_list (self):
        valuelist = [1,2,3]
        self.assertEqual(6, Addition.sum(valuelist))



if __name__ == '__main__':
    unittest.main()
