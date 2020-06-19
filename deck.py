from card import Card
import random
import math


class Deck:
    __STANDARD_DECK = [Card(i, suit) for i in range(1, 14) for suit in ('Heart', 'Diamond', 'Spade', 'Club')]

    def __init__(self, deck=None, shuffled=False, n_decks=1):
        self.__deck = self.__STANDARD_DECK if deck is None else deck
        self.__deck *= n_decks
        self.__size = len(self.__deck)
        if shuffled:
            self.shuffle()

    def __len__(self):
        return len(self.__deck)

    def __swap(self, i, j):
        self.__deck[i], self.__deck[j] = self.__deck[j], self.__deck[i]

    def shuffle(self):
        for i in range(self.__size):
            random_card_index = math.floor((random.uniform(0, self.__size)))
            self.__swap(i, random_card_index)

    def deal(self):
        return self.__deck.pop()

    def __str__(self):
        return ''.join([card.get_let()+'\n' for card in self.__deck])

