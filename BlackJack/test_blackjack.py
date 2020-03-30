import unittest
import math
import blackjack as bj


class CardTestCase(unittest.TestCase):
        """Unit tests for Blackjack Card class"""
    def test_value_of_card(self):
        """Does card return correct value?"""
        card = Card("5")
        self.assertEqual(card.value(), 5)
        card = Card("A")
        self.assertEqual(card.value(), 11)
        card = Card("J")
        self.assertEqual(card.value(), 10)


