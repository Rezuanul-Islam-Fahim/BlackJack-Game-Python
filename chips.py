class Chips:

    def __init__(self):
        self.total = 0
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet