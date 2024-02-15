from collections import defaultdict

from constants import NO_OF_ITEMS, GROUP_PRICE
from .item import Item

class SuperMarket:
    def __init__(self, items_inventory: dict = {}, special_prices_inventory: dict = {}) -> None:
        self._items_inventory = items_inventory
        self._special_prices_inventory = special_prices_inventory

    def update_items_inventory(self, items_inventory) -> None:
        self._items_inventory = items_inventory

    def update_special_prices_inventory(self, special_prices_inventory) -> None:
        self._special_prices_inventory = special_prices_inventory

    def _find_normal_item_cost(self, item_count: int, item: Item) -> float:
        total_item_cost = item_count*item.get_unit_price()
        return total_item_cost
    
    def _find_special_offer_item_cost(self, item_count: int, item: Item, special_price_parameters: dict) -> float:
        no_of_items = special_price_parameters[NO_OF_ITEMS]
        
        no_of_groups = item_count // no_of_items
        remaining_items_count = item_count % no_of_items
        
        group_items_cost = no_of_groups * special_price_parameters[GROUP_PRICE]
        remaining_individual_items_cost = remaining_items_count*item.get_unit_price()  
        total_item_cost =  group_items_cost + remaining_individual_items_cost

        return total_item_cost
    
    def _get_item_cost(self, item_name: str, item_count: int) -> float:
        item = self._items_inventory.get(item_name)
        if not item:
            raise Exception("Item not found in inventory. Halting checkout!")

        special_price_parameters = self._special_prices_inventory.get(item_name)
        if special_price_parameters:
            item_cost = self._find_special_offer_item_cost(item_count, item, special_price_parameters)
        else:
            item_cost = self._find_normal_item_cost(item_count, item)

        return item_cost

    def checkout_items(self, items_bought_stream: str) -> float:
        items_count = defaultdict(int)
        total_checkout_cost = 0.0

        for item_name in items_bought_stream:
            items_count[item_name] += 1

        for item_name, item_count in items_count.items():
            total_checkout_cost += self._get_item_cost(item_name, item_count)
            
        return total_checkout_cost