from line_item import LineItem


class Cart:
    __line_item = LineItem()

    @staticmethod
    def get_line_item():
        if not isinstance(Cart.__line_item, LineItem):
            Cart.clear()
        return Cart.__line_item

    @staticmethod
    def get_total():
        if not isinstance(Cart.__line_item, LineItem):
            return 0
        return Cart.__line_item.get_total()

    @staticmethod
    def clear():
        Cart.__line_item = LineItem()
