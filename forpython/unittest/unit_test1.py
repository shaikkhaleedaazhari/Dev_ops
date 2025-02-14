import unittest  # Missing import

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_number(self):
        self.assertEqual(add(2, 4), 6, "Expected 6 but got something else.")

    def test_add_negative(self):
        self.assertEqual(add(-4, -2), -6, "Expected -6 but got something else.")

if __name__ == "__main__":
    unittest.main()  # Removed extra dots


