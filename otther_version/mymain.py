import unittest
from cart import Cart
from line_item import LineItem


def main():
    Cart.get_line_item().add()
    print(Cart.get_total())


if __name__ == '__main__':
    main()
