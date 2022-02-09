import unittest
from cart import Cart
from line_item import LineItem
from promotion import Promotion
from cast_promotion import CastPromotion


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

    def test_add_multiple(self):
        Cart.clear()
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('carrot', 33.9)
        Cart.get_line_item().add('carrot', 33.9)
        Cart.get_line_item().add('carrot', 33.9)
        Cart.get_line_item().add('carrot', 33.9)
        self.assertEqual(30*3 + 33.9*4, Cart.get_total())

    def test_discount_percentage(self):
        Cart.clear()
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('carrot', 33.9)
        self.assertEqual((30+33.9) * (1-0.3),
                         Promotion(0.3).cast(Cart.get_total()))

    def test_discount_fixed(self):
        Cart.clear()
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('carrot', 33.9)
        self.assertEqual(round((30+33.9-20), 2),
                         Promotion(fixed=20).cast(Cart.get_total()))

    def test_discount_both(self):
        Cart.clear()
        Cart.get_line_item().add('apple', 30)
        Cart.get_line_item().add('carrot', 33.9)
        self.assertEqual(round((30+33.9-20) * (1-0.3), 2),
                         Promotion(0.3, 20).cast(Cart.get_total()))


if __name__ == '__main__':
    unittest.main()
