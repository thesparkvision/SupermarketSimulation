from models import Item, SuperMarket
from constants import ITEMS_INVENTORY, SPECIAL_PRICES_INVENTORY

supermarket_instance = None

def get_supermarket_instance():
    global supermarket_instance
    if supermarket_instance:
        return supermarket_instance

    supermarket = SuperMarket()

    supermarket.update_items_inventory(ITEMS_INVENTORY)
    supermarket.update_special_prices_inventory(SPECIAL_PRICES_INVENTORY)
    supermarket_instance = supermarket

    return supermarket_instance

def run_custom_supermarket_simulation() -> None:
    supermarket = get_supermarket_instance()    

    items_bought_stream = input("Enter Items: ")
    total_checkout_cost = supermarket.checkout_items(items_bought_stream)

    print(f"Total Checkout cost for the bought items is: {total_checkout_cost} cents (INR)")

def run_configured_supermarket_simulation() -> None:
    supermarket = get_supermarket_instance()

    test_cases = [
        {
            "input": "",
            "expected_output": 0
        },
        {
            "input": "A",
            "expected_output": 50
        },
        {
            "input": "AB",
            "expected_output": 80
        },
        {
            "input": "CDBA",
            "expected_output": 115
        },
        {
            "input": "AA",
            "expected_output": 100
        },
        {
            "input": "AAA",
            "expected_output": 130
        },
        {
            "input": "AAAA",
            "expected_output": 180
        },
        {
            "input": "AAAAA",
            "expected_output": 230
        },
        {
            "input": "AAAAAA",
            "expected_output": 260
        },
        {
            "input": "AAAB",
            "expected_output": 160
        },
        {
            "input": "AAABB",
            "expected_output": 175
        },
        {
            "input": "AAABBD",
            "expected_output": 190
        },
        {
            "input": "DABABA",
            "expected_output": 190
        }
    ]
  
    for test_case in test_cases:
        input_items = test_case["input"]
        expected_output = test_case["expected_output"]

        print(f"Validating Total Cost for input {input_items} is {expected_output} cents (INR)")

        total_checkout_cost = supermarket.checkout_items(input_items)
        print("VERDICT: PASS" if total_checkout_cost == expected_output else "VERDICT: FAIL")