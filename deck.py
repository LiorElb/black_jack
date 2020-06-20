from card import Card, Suit
import random
import math


class Deck:
    STANDARD_DECK = [Card(value, suit) for value in range(1, 14) for suit in Suit]

    def __init__(self, deck=None, shuffled=False, n_decks=1):
        if deck is None:
            deck = self.STANDARD_DECK
        self._deck = deck
        self._deck *= n_decks
        if shuffled:
            self.shuffle()

    def __len__(self):
        return len(self._deck)

    def __swap(self, i, j):
        self._deck[i], self._deck[j] = self._deck[j], self._deck[i]

    def shuffle(self):
        for i in range(len(self)):
            random_card_index = math.floor((random.uniform(0, len(self))))
            self.__swap(i, random_card_index)

    def deal(self):
        return self._deck.pop()

    def __repr__(self):
        return str(self._deck)


print(Deck(shuffled=True))
