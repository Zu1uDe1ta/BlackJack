import os
import random

card_rank = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")

hand = []
dealer = []
player = []


def value_of_card(hand):
    non_aces = [card for card in hand if card != 'A']
    sum = 0
    for card in non_aces:
        if card in 'JQK':
            sum += 10
    else:
        sum += int(card)

def card_is_ace():
        aces = [card for card in hand if card == 'A']
        for card in aces:
            if sum <= 10:
                sum += 11
        else:
            sum += 1
        return sum


while True:
    cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    ]

def shuffle():
    random.shuffle(cards)

def deal():
    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())
    dealer.append(cards.pop())

    first_hand = True
    standing = False

    while True:
        os.system('clear')

        player_score = value_of_card(player)
        dealer_score = value_of_card(dealer)

        if standing:
            print('Dealer: [{}] ({})'.format(']['.join(dealer), dealer_score))
        else:
            print('Dealer: [{}][?]'.format(dealer[0]))

        print('You:   [{}] ({})'.format(']['.join(player), player_score))
        print('')

        if standing:
            if dealer_score > 21:
                print('Dealer busted, you win!')
            elif player_score == dealer_score:
                print('Push, nobody wins')
            elif player_score > dealer_score:
                print('You beat the dealer, you win!')
            else:
                print('You lose, try again!')

            print('')
            input('Play again? Hit enter to continue')
            break

        if first_hand and player_score == 21:
            print('Blackjack! Nice!')
            print('')
            input('Play again? Hit enter to continue')
            break

        if player_score > 21:
            print('You busted!')
            print('')
            input('Play again? Hit enter to continue')
            break

        print('What would you like to do?')
        print(' [1] Hit')
        print(' [2] Stand')

        print('')
        choice = input('Your choice: ')
        print('')

        first_hand = False

        if choice == '1':
            player.append(cards.pop())
        elif choice == '2':
            standing = True
            while value_of_card(dealer) <= 16:
                dealer.append(cards.pop())
































##################


import random
import time
from termcolor import colored, COLORS

CARD_RANK = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
CARD_SUIT = ("♡", "♢", "♧", "♤")
SYSTEM_COLORS = ['grey', 'white']
PLAYER_COLORS = list(c for c in COLORS.keys() if c not in SYSTEM_COLORS)

class Card(object):
    """Represents an individual playing card"""

    def __init__(self, rank, suit):
        assert rank in CARD_RANK
        self.rank = rank
        assert suit in CARD_SUIT
        self.suit = suit

    def __repr__(self):
        return "{:>2}{}".format(self.rank, self.suit)

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
        """Represents deck of 52 cards to be dealt to the player and dealer"""

        def __init__(self):
            self.__new_deck()

        def __new_deck(self):
            """Create a new deck of 52 cards"""
            self.cards = list(Card(r, s) for r in CARD_RANK for s in CARD_SUIT)

        def shuffle(self):
            """Randomly shuffle the deck of cards"""
            random.shuffle(self.cards)

        def deal(self):
            """Deal from the end of the deck - if the deck is empty, start a new one"""
            if not self.cards:
                self.__new_deck()
                self.shuffle()
            return self.cards.pop()

        class Hand(object):
            """Represents the cards held by the player or the dealer"""

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