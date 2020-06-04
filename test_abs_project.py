import unittest

class TestAbs(unittest.TestCase):
    def test_x(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_y(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()