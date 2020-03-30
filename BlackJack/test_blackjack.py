import unittest
import math
import blackjack as bj


class CardTestCase(unittest.TestCase):

    def test_value_of_card(self):
        card = Card("5")
        self.assertEqual(card.value(), 5)
        card = Card("A")
        self.assertEqual(card.value(), 11)
        card = Card("J")
        self.assertEqual(card.value(), 10)


