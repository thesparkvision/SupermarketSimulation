import unittest
from collections import defaultdict

from models import SuperMarket, Item

class TestSuperMarket(unittest.TestCase):
    def setUp(self):
        self.items_inventory = {
            "A": Item("A", 50),
            "B": Item("B", 75),
            "C": Item("C", 100)
        }

        self.special_prices_inventory = {
            "A": {"no_of_items": 2, "group_price": 80},
        }

        self.supermarket = SuperMarket()
        self.supermarket.update_items_inventory(self.items_inventory)
        self.supermarket.update_special_prices_inventory(self.special_prices_inventory)

    def test_normal_item_checkout(self):
        """Check if the total cost is calculated correctly when the items have no special offer"""

        total_cost = self.supermarket.checkout_items("BCCBB")
        
        self.assertAlmostEqual(total_cost, 425.0)

    def test_special_offer_item_checkout(self):
        """Check if the total cost is calculated correctly when the items have special offer"""
   
        supermarket = SuperMarket(self.items_inventory, self.special_prices_inventory)

        total_cost = supermarket.checkout_items("ABCAAAA")
        
        self.assertAlmostEqual(total_cost, 385.0)

    def test_item_not_found(self):
        """Testing Checkout Failure on some items not in the inventory"""

        supermarket = SuperMarket(self.items_inventory, self.special_prices_inventory)

        with self.assertRaises(Exception):
            supermarket.checkout_items("ABM")