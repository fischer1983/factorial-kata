import unittest
from Factorial import Factorial

class FactorialTest(unittest.TestCase):

    def test_calculate(self):
        factorial = Factorial()
        self.assertEqual(5, factorial.calculate(0))

if __name__ == '__main__':
    unittest.main()