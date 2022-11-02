from deck import *
from hand import *
from chips import *
from functions import *


def main():
    playing = True

    while True:
        print('Welcome to BlackJack')

        deck = Deck()
        deck.shuffle_deck()

        player_hand = Hand()
        player_hand.add_card(deck.deal_one())
        player_hand.add_card(deck.deal_one())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

        player_chips = Chips()
        take_bet(player_chips)
        show_some(dealer_hand, player_hand)

        while playing:
            hit_or_stand(deck, player_hand)
            show_some(dealer_hand, player_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all(dealer_hand, player_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print('\nPlayer\'s winnings stand at {}'.format(player_chips.total))

        new_game = input('Would you like to play again (y/n): ')

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
