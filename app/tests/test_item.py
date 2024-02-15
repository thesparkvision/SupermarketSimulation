import unittest

from app.models.item import Item

class TestItem(unittest.TestCase):
    def test_get_unit_price(self):
        """Check if the get_unit_price method returns the correct unit price"""

        item = Item("A", 0.5)
        
        self.assertEqual(item.get_unit_price(), 0.5)

    def test_initialization(self):
        """Check if the name and unit_price attributes are set correctly during initialization"""

        item = Item("B", 0.75)
        
        self.assertEqual(item._name, "B")
        self.assertEqual(item._unit_price, 0.75)