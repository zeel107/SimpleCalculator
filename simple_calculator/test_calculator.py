import unittest
from simple_calculator.calculator import Calculator
import math

class calctest(unittest.TestCase):



    def test_sum(self):
        c = Calculator()
        self.assertEqual(c.calculate("1+1"), 2)
        self.assertEqual(c.calculate("3+-5"), -2)
        self.assertEqual(c.calculate("-0+1"), 1)
        self.assertEqual(c.calculate("0.125+10"), 10.125)

    def test_subtract(self):
        c = Calculator()
        self.assertEqual(c.calculate("1-1"), 0)

    def test_multiply(self):
        c = Calculator()
        self.assertEqual(c.calculate("1*1"), 1)
        self.assertEqual(c.calculate("2*5"), 10)
        self.assertEqual(c.calculate("5*3*2"), 30)

    def test_divide(self):
        c = Calculator()
        self.assertEqual(c.calculate("2/10"), .2)

    def test_exponent(self):
        c = Calculator()
        self.assertEqual(c.calculate("2^3"), 8)
        self.assertEqual(c.calculate("2^(1/2)"), math.sqrt(2))

    def test_urinary(self):
        c = Calculator()
        self.assertEqual(c.calculate("sin(0)"), 0)
        self.assertEqual(c.calculate("cos(0)"), 1)
        self.assertEqual(c.calculate("tan(0)"), 0)
        self.assertEqual(c.calculate("cot(0)"), 0)
        self.assertEqual(c.calculate("log(100)"), 2)
        self.assertEqual(c.calculate("ln(1)"), 0)

    def test_undefined(self):
        c = Calculator()
        self.assertEqual(c.calculate("1/0"), "undefined")

    def test_unformatted_input(self):
        c = Calculator()
        self.assertEqual(c.calculate())


if __name__ == '__main__':
    unittest.main()