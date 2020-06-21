import typing
from enum import Enum

from blackjack_dealer import BlackJackDealer
from blackjack_hand import BlackJackHand
from blackjack_player import BlackJackPlayer
from deck import Deck
from io_manager import IOManager


class WinStatus(Enum):
    BLACKJACK = 'BlackJack'
    WIN = 'Win'
    PUSH = 'Push'
    BUST = 'Bust'
    LOSS = 'Loss'


class Game:
    # noinspection PyShadowingNames
    def __init__(self, deck: Deck = None, player: BlackJackPlayer = None):
        if deck is None:
            deck = Deck(shuffled=True, n_decks=8)
        if player is None:
            player = BlackJackPlayer()
        self.__deck = deck
        self._dealer = BlackJackDealer()
        self.player = player
        self._io_manager = IOManager()

    def play_round(self):
        self._dealer.hand = self.deal_new_hand()
        self.player.hands = [self.deal_new_hand()]
        self._get_bet_from_user()
        for hand in self.player.hands:
            self.play_hand(hand)
        if not (self.player.all_bust() or self.player.all_blackjack()):
            self._dealer.play_turn()
        self._io_manager.show_dealer_hand_to_user(self._dealer.hand, upcard_only=False)
        self._process_winnings(self.player.hands, self._dealer.hand)

    def play_hand(self, hand: BlackJackHand):
        choice = 0
        while choice != 2 and hand.sum < 21:
            self._io_manager.print_turn_status(self.player, hand, self._dealer)
            if hand.is_blackjack():
                return
            self._io_manager.show_player_options(hand)
            choice = self._io_manager.get_player_choice()
            if choice == 1:
                self._dealer.deal_to(hand)
            if choice == 4:
                return self.double_down(hand)
            if choice == 3:
                self.split_hand(hand)
        self._io_manager.print_end_turn_message(hand)

    def deal_new_hand(self):
        new_hand = BlackJackHand()
        self._dealer.deal_to(new_hand, 2)
        return new_hand

    def _get_bet_from_user(self):
        bet = self._io_manager.get_player_bet()
        self.player.bank -= bet
        self.player.hands[0].bet_size = bet

    def split_hand(self, hand: BlackJackHand):
        new_hand = BlackJackHand()
        self.player.bank -= hand.bet_size
        new_hand.bet_size = hand.bet_size
        hand.transfer_last_card_to(new_hand)
        self.player.hands.append(new_hand)
        self._dealer.deal_to(hand)
        self._dealer.deal_to(new_hand)

    def double_down(self, hand: BlackJackHand):
        self.player.bank -= hand.bet_size
        hand.bet_size *= 2
        self._dealer.deal_to(hand)
        return

    def is_winning(self, player_hand: BlackJackHand):
        return player_hand.sum <= 21 and (player_hand.sum < self._dealer.hand.sum or self._dealer.hand.sum > 21)

    def _process_winnings(self, player_hands: typing.List[BlackJackHand], dealer_hand: BlackJackHand):
        for hand in player_hands:
            if hand.is_blackjack():
                winnings_sum = hand.bet_size * 2.5
                winnings_status = WinStatus.BLACKJACK
            elif hand.sum <= 21 and (dealer_hand.sum < hand.sum or dealer_hand.sum > 21):
                winnings_sum = hand.bet_size * 2
                winnings_status = WinStatus.WIN
            elif dealer_hand.sum == hand.sum <= 21:
                winnings_sum = hand.bet_size
                winnings_status = WinStatus.PUSH
            else:
                winnings_sum = 0
                winnings_status = WinStatus.BUST if hand.sum > 21 else WinStatus.LOSS
            self._io_manager.print_winnings_to_player(winnings_sum, winnings_status.value)
            self.player.bank += winnings_sum


game_deck = Deck(shuffled=True, n_decks=8)
player = BlackJackPlayer(bank=1000)
my_game = Game(game_deck, player)
my_game.play_round()
