import random
from data import suits, ranks
from card import *


class Deck:

    def __init__(self):
        self.card_list = []

        for suit in suits:
            for rank in ranks:
                self.card_list.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.card_list)

    def deal_one(self):
        return self.card_list.pop()

    def __str__(self):
        deck_comp = ''

        for card in self.card_list:
            deck_comp += card.__str__() + '\n'

        return deck_comp
