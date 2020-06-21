from blackjack_hand import BlackJackHand
from deck import Deck


class BlackJackDealer:
    def __init__(self, hand: BlackJackHand = None, deck: Deck = None):
        if hand is None:
            hand = BlackJackHand()
        if deck is None:
            deck = Deck()
        self.hand = hand
        self._deck = deck

    def deal_to(self, hand, n_cards=1):
        for i in range(n_cards):
            hand.add(self._deck.deal())

    def play_turn(self):
        while self.hand.sum < 17:
            self.deal_to(self.hand)

    def __repr__(self):
        return str(self.hand)
