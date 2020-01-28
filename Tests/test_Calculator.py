import unittest




class MyTestCase(unittest.TestCase):






    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()