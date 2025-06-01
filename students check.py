import unittest

# division.py
def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b



class TestSafeDivide(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(safe_divide(10, 2), 5)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_divide(5, 0)

if __name__ == '__main__':
    unittest.main()