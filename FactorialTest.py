import unittest
from Factorial import Factorial

class FactorialTest(unittest.TestCase):

    def test_calculate(self):
        factorial = Factorial()
        self.assertEqual(15511210043330985984000000, factorial.calculate(25))

if __name__ == '__main__':
    unittest.main()