import unittest
from newproj import calc


class test_calc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(15, 16), 31)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -3), -4)

    def test_sub(self):
        self.assertEqual(calc.sub(16, 12), 4)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(-1, -1), 0)
        self.assertEqual(calc.sub(1, -1), 2)

    def test_mul(self):
        self.assertEqual(calc.multiply(2, 5), 10)
        self.assertEqual(calc.multiply(-2, 1), -2)
        self.assertEqual(calc.multiply(-3, -1), 3)
        self.assertEqual(calc.multiply(1, -1), -1)

    def test_divide(self):
        self.assertEqual(calc.divide(2, 5), 0.4)
        self.assertEqual(calc.divide(-2, 1), -2)
        self.assertEqual(calc.divide(-3, -1), 3)
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
