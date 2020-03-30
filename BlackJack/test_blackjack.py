import unittest
import math
import blackjack as bj


class CardTestCase(unittest.TestCase):


def test_value_of_card(self):
    card = card("5")
    self.assertEqual(card.value(), 5)
    card = card("A")
    self.assertEqual(card.value(), 11)
    card = card("J")
    self.assertEqual(card.value(), 10)


def test_shuffle(self):
    deck_one = Deck()
    deck_one.shuffle()
    deck_two = Deck()
    deck_two.shuffle()
    self.assertNotEqual(str(deck_one), str(deck_two))

def test_deal(self):
    deck = Deck()
    num_before = len(deck.cards)
    deck.deal()
    num_after = len(deck.cards)
    self.assertEqual(num_before, num_after + 1)
