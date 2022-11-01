def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?: '))
        except ValueError:
            print('Please enter a number')
        else:
            if chips.bet > chips.total:
                print(
                    f'Sorry, you don\'t have enough chips. You have {chips.total} chips')
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or stand. Enter h or s: ')

        if x == 'h':
            hit(deck, hand)
        elif x == 's':
            print('Player stands. Dealer\'s turn.')
            playing = False
        else:
            print('Sorry. I didn\'t understand.')
            continue

        break


def show_some(dealer, player):
    print('\nDealer\'s hand: ')
    print('First card hidden')
    print(dealer.cards[1])

    print('\nPlayer\'s hand: ')
    for card in player.hand:
        print(card)


def show_all(dealer, player):
    print('\nDealer\'s items: ')
    for card in dealer.cards:
        print(card)
    print(f'Value of Dealer\'s hand: {dealer.value}')

    print('\nPlayer\'s items: ')
    for card in player.cards:
        print(card)
    print(f'Value of Player\'s hand: {player.value}')


def player_busts(player, dealer, chips):
    print('BUST Player')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('BUST Dealer')
    chips.lose_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer wins')
    chips.win_bet()


def push(player, dealer):
    print('Player and Dealer tie. PUSH!!!')
