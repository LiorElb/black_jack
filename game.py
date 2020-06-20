from blackjack_dealer import BlackJackDealer
from blackjack_player import BlackJackPlayer
from deck import Deck
from blackjack_hand import BlackJackHand
from blackjack_dealer import BlackJackDealer
from card import Card
import typing

from io_manager import IOManager


class Game:
    def __init__(self, deck: Deck = None):
        if deck is None:
            deck = Deck(shuffled=True, n_decks=8)
        self.__deck = deck
        self._dealer = BlackJackDealer()
        self._player = BlackJackPlayer()
        self._io_manager = IOManager()

    def play_round(self):
        self._dealer.hand = self.deal_new_hand()
        self._player.hands = [self.deal_new_hand()]
        self._get_bet_from_user()
        for hand in self._player.hands:
            self.play_hand(hand)
        self._dealer.play_turn()
        self._io_manager.show_hand_to_user(self._dealer.hand)
        for hand in self._player.hands:
            is_winning = check_for_win(hand, self._dealer.hand)

    def play_hand(self, hand):
        choice = 0
        while choice != 2 and hand.sum < 21:
            self._io_manager.print_turn_status(self._player, hand, self._dealer)
            choice = self._io_manager.get_player_choice()
            if choice == 1:
                self._dealer.deal_to(hand)
            if choice == 4:
                return self.double_down(hand)
            if choice == 3:
                self.split_hand(hand)

    def deal_new_hand(self):
        new_hand = BlackJackHand()
        self._dealer.deal_to(new_hand, 2)
        return new_hand

    def _get_bet_from_user(self):
        bet = self._io_manager.get_player_bet()
        self._player.bank -= bet
        self._player.hands[0].bet_size = bet

    def split_hand(self, hand):
        new_hand = BlackJackHand()
        hand.transfer_last_card_to(new_hand)
        self._player.hands.append(new_hand)
        self._dealer.deal_to(hand)
        self._dealer.deal_to(new_hand)

    def double_down(self, hand):
        self._player -= hand.bet_size
        hand.bet_size *= 2
        self._dealer.deal_to(hand)
        return


game_deck = Deck(shuffled=True, n_decks=8)
my_game = Game(game_deck, 10000)
my_game.play_round()
