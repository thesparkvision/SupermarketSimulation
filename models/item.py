class Item:
    def __init__(self, name: str, unit_price: float):
        self._name = name
        self._unit_price = unit_price

    def get_unit_price(self):
        return self._unit_price