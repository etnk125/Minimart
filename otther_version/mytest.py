import unittest
from cart import Cart
from line_item import LineItem


class MyTest(unittest.TestCase):
    def test_zero(self):
        Cart.clear()
        Cart.get_line_item().add()
        self.assertEqual(0, Cart.get_total())

    def test_add_two(self):
        Cart.clear()
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('carrot', 33.9)
        self.assertEqual(30+33.9, Cart.get_total())

    def test_add_three(self):
        Cart.clear()
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('carrot', 33.9)
        Cart.get_line_item().add('carrot', 33.9)
        Cart.get_line_item().add('carrot', 33.9)
        Cart.get_line_item().add('carrot', 33.9)
        self.assertEqual(30*3+33.9*4, Cart.get_total())
    # def test_zero(self):
    #     Cart.get_line_item().add()
    #     self.assertEqual(0, Cart.get_total())

    # def test_zero(self):
    #     Cart.get_line_item().add()
    #     self.assertEqual(0, Cart.get_total())


if __name__ == '__main__':
    unittest.main()
