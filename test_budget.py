# test_module.py
import unittest
from budget import Category, create_spend_chart

class TestCategory(unittest.TestCase):
    def setUp(self):
        self.food = Category("Food")

    def test_deposit(self):
        self.food.deposit(100, "initial deposit")
        self.assertEqual(self.food.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()