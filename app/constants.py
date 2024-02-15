from app.models.item import Item

NO_OF_ITEMS = "no_of_items"
GROUP_PRICE = "group_price"

ITEMS_INVENTORY = {
    "A": Item(
        name="A", 
        unit_price=50.0
    ),
    "B": Item(
        name="B", 
        unit_price=30.0
    ),
    "C": Item(
        name="C", 
        unit_price=20.0
    ),
    "D": Item(
        name="D", 
        unit_price=15.0
    )
}

SPECIAL_PRICES_INVENTORY = {
    "A": {
            NO_OF_ITEMS: 3,
            GROUP_PRICE: 130.0
    },
    "B": {
            NO_OF_ITEMS: 2,
            GROUP_PRICE: 45
    }
}