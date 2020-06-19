class Card:
    _COLOR_OF = {
        'Heart': 'Red',
        'Diamond': 'Red',
        'Spade': 'Black',
        'Club': 'Black',
        None: None
    }
    _VALUE_OF = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }
    _NAME_OF = {
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': '10',
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King',
        'A': 'Ace'
    }
    _LETTER_OF = {
        1: 'A',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: 'J',
        12: 'Q',
        13: 'K'
    }

    def __init__(self, let=None, shape=None):
        self.__letter = self._LETTER_OF[let] if type(let) is int else let.capitalize() if type(let) is str else let
        self.__suit = shape.capitalize() if type(shape) is str else shape
        self.__color = self._COLOR_OF[self.__suit]
        self.__name = self._NAME_OF[self.__letter]
        self.__value = self._VALUE_OF[self.__letter]

    def get_suit(self): return self.__suit

    def get_color(self): return self.__color

    def get_let(self): return self.__letter

    def get_name(self): return self.__name

    def is_ace(self): return self.__letter == 'A'

    def get_value(self): return self.__value

    def __str__(self):
        return f"This is the {self._NAME_OF[self.__letter]} of {self.__suit}s"

    def __lt__(self, other):
        return self.__value < other.get_value()

    def __le__(self, other):
        return self.__value <= other.get_value()

    def __eq__(self, other):
        return self.__value == other.get_value()

    def __ne__(self, other):
        return self.__value != other.get_value()

    def __gt__(self, other):
        return self.__value > other.get_value()

    def __ge__(self, other):
        return self.__value >= other.get_value()
