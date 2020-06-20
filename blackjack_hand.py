from card import Card, Suit
import typing


class BlackJackHand:
    cards: typing.List[Card]
    bet_size: float = 0
    ace_count: int

    def __init__(self, cards: typing.List[Card] = None):
        if cards is None:
            cards = []
        self._cards = cards
        self._sum = 0
        self._add_cards(cards)

    def add(self, card: Card):
        if card.is_ace():
            self.ace_count += 1
        if card.is_ace() and self._sum >= 11:
            self._sum += 1
        else:
            self._sum += card.value
        self._cards.append(card)

    def _add_cards(self, cards: typing.List[Card]):
        for card in cards:
            self.add(card)

    def can_split(self):
        return len(self) == 2 and self._cards[0].value == self._cards[1].value

    def transfer_last_card_to(self, other):
        other.add(self._cards.pop())

    def __repr__(self):
        return str(self._cards)

    def __len__(self):
        return len(self._cards)

    @property
    def sum(self):
        return self._sum
