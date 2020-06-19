class Hand:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self._cards = cards
        self._sum = 0
        self._count_sum()

    def _count_sum(self):
        temp_sum = 0
        for card in self._cards:
            if temp_sum < 11:
                temp_sum += card.get_value()
            else:
                temp_sum += 1 if card.is_ace() else card.get_value()
        self._sum = temp_sum

    def get_sum(self):
        return self._sum

    def as_dealer(self):
        return f'[X,{self._cards[-1].get_let()}]'

    def add(self, card):
        if card.is_ace() and self._sum >= 11:
            self._sum += 1
        else:
            self._sum += card.get_value()
        self._cards.append(card)

    def can_split(self):
        return len(self) == 2 and self._cards[0] == self._cards[1]

    def transfer_to(self, other, i=-1):
        other.add(self._cards.pop(i))

    def __lt__(self, other):
        return self._sum < other.get_sum()

    def __le__(self, other):
        return self._sum <= other.get_sum()

    def __ge__(self, other):
        return self._sum >= other.get_sum()

    def __gt__(self, other):
        return self._sum > other.get_sum()

    def equals(self, other):
        return self._sum == other.get_sum()

    def __str__(self):
        return f"[{','.join([card.get_let() for card in self._cards])}]"

    def __len__(self):
        return len(self._cards)
