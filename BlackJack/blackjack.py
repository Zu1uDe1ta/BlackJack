import os
import random

card_rank = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")

hand = []
dealer = []
player = []




def value_of_card(hand):
    non_aces = [card for card in hand if card != 'A']
    aces = [card for card in hand if card == 'A']
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


while True:
    cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    ]


    random.shuffle(cards)
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
