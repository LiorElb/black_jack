from enum import Enum


class Suit(Enum):
    HEART = 'Heart'
    DIAMOND = 'Diamond'
    SPADE = 'Heart'
    CLUB = 'Club'


class Card:

    def __init__(self, value: int, suit: Suit):
        self._value = value
        self._suit = suit

    @property
    def value(self):
        return self._value

    @property
    def letter(self):
        if self._value == 1:
            return 'A'
        if self._value == 11:
            return 'J'
        if self._value == 12:
            return 'Q'
        if self._value == 13:
            return 'K'
        return str(self._value)

    @property
    def name(self):
        if self._value == 1:
            return 'Ace'
        if self._value == 11:
            return 'Jack'
        if self._value == 12:
            return 'Queen'
        if self._value == 13:
            return 'King'
        return str(self._value)

    def is_ace(self):
        return self._value == 1

    def __repr__(self):
        return f'{self.name} of {self._suit.value}s'


