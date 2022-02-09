
class LineItem:
    def __init__(self):
        self._items = []
        self._total = 0

    def add(self, name=None, price=0.0):
        if isinstance(name, str):
            self._items.append((name, float(price)))
            self.update_total(float(price))

    def update_total(self, price):
        self._total += price

    def get_total(self):
        return round(self._total, 2)
