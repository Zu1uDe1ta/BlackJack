from __future__ import print_function
import random
import os
from builtins import input
import time


cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
]
rank = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")

dealer = []
you = []
player = []


class Card(object):
    """Represents an individual playing card"""
    def value(self):
        """Computes the value of a card according to Blackjack rules"""
        if self.ace():
            value = 11
        else:
            try:
                value = int(self.rank)
            except ValueError:
                value = 10
        return value

    def ace(self):
        """Is this card an ace?"""
        return self.rank == "A"

class Deck(object):
    def deal(self):
        random.shuffle(cards)
        player.append(cards.pop())
        you.append(cards.pop())
        dealer.append(cards.pop())
        player.append(cards.pop())
        you.append(cards.pop())
        dealer.append(cards.pop())

class Hand(object):
    """Represents the cards held by the player or the dealer"""

    def calc_hand(hand):
        non_aces = [c for c in hand if c != 'A']
        aces = [c for c in hand if c == 'A']
        sum = 0
        for card in non_aces:
            if card in 'JQK':
                sum += 10
            else:
                sum += int(card)
        for card in aces:
            if sum <= 10:
                sum += 11
            else:
                sum += 1
        return sum





    def __init__(self, stake=0):
        self.cards = []
        self.stake = stake
        self.active = True

    def __repr__(self):
        return "  ".join(str(card) for card in self.cards)

    def first(self):
        """Returns the first card in the hand"""
        assert self.cards
        return self.cards[0]

    def last(self):
        """Returns the last card in the hand"""
        assert self.cards
        return self.cards[-1]

    def add_card(self, card):
        """Add the instance of card to the hand"""
        self.cards.append(card)

    def value(self):
        """Calculate the value of the hand, taking into account Aces can be 11 or 1"""
        aces = sum(1 for c in self.cards if c.ace())
        value = sum(c.value() for c in self.cards)
        while value > 21 and aces > 0:
            aces -= 1
            value -= 10
        return value

    def blackjack(self):
        """Determine if the hand is 'blackjack'"""
        return len(self.cards) == 2 and self.value() == 21

    def twenty_one(self):
        """Determine if the hand is worth 21"""
        return self.value() == 21

    def bust(self):
        """Determine if the hand is worth more than 21, known as a 'bust'"""
        return self.value() > 21

    def pair(self):
        """Determine if the hand is two cards the same"""
        return len(self.cards) == 2 and self.first().rank == self.last().rank

    def split(self):
        """Split this hand into two hands if it can be split"""
        assert self.pair()
        card = self.cards.pop()
        hand = Hand(self.stake)
        hand.add_card(card)
        return hand


# Compare the sums of the cards between D v P
# If P card sum is greater than 21 = BUST
# If P card sum is less than 21 = Option Hit or Stay
# If P option Stay compare sum of D v P
# If P sum < 21 && > D sum then P wins!
# If P sum < D sum then P loses



random.shuffle(cards)




if __name__ == '__main__':
    main()
