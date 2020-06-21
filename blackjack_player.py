class BlackJackPlayer:
    def __init__(self, bank: int = 0):
        self.hands = []
        self.bank = bank

    def add_to_bank(self, amount):
        self.bank += amount

    def remove_from_bank(self, amount):
        self.bank -= amount

    def all_bust(self):
        for hand in self.hands:
            if hand.sum <= 21:
                return False
        return True

    def all_blackjack(self):
        for hand in self.hands:
            if not hand.is_blackjack():
                return False
        return True
