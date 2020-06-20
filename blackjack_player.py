import typing

from blackjack_hand import BlackJackHand
from card import Card


class BlackJackPlayer:
    def __init__(self, hands: typing.List[BlackJackHand] = None, bank: int = 0):
        if hands is None:
            hands = []
        self.hands = hands
        self.bank = bank

    def add_to_bank(self, amount):
        self.bank += amount

    def remove_from_bank(self, amount):
        self.bank -= amount

