from deck import Deck
from hand import Hand
from card import Card


class Game:
    def __init__(self, deck=None, player_bank=0):
        if deck is None:
            self.__deck = Deck(shuffled=True, n_decks=8)
        else:
            self.__deck = deck
        self.__player_bank = player_bank
        self._pot = 0

    def deal_to(self, hand, n_cards=1):
        for i in range(n_cards):
            hand.add(self.__deck.deal())

    def shuffle_deck(self):
        self.__deck.shuffle()

    def get_player_bank(self):
        return self.__player_bank

    def add_funds_to_player(self, amount=0):
        self.__player_bank += amount

    def __print_turn_status(self, player_hand, dealer_hand, bet):
        print('Dealers hand: ', dealer_hand.as_dealer())
        print('Your hand: ', player_hand)
        print(f'Bank: {self.__player_bank}\t Pot: {self._pot}\t Bet Size: {bet}')
        print('1.Hit\n2.Stand')
        if player_hand.can_split():
            print('3.Split')
        if len(player_hand) == 2:
            print('4.Double Down')

    def play_hand(self, player_hand, dealer_hand, bet, player_hands):
        self.__print_turn_status(player_hand, dealer_hand, bet)
        choice = input()
        while choice != '2':
            if choice in ('1', '4'):
                self.deal_to(player_hand)
                if choice == '4':
                    self.__player_bank -= bet
                    self._pot += bet
                    break
            elif choice == '3':
                new_hand = Hand()
                player_hand.transfer_to(new_hand)
                self.deal_to(player_hand)
                self.deal_to(new_hand)
                player_hands.append(new_hand)
            self.__print_turn_status(player_hand, dealer_hand, bet)
            choice = input() if player_hand.get_sum() < 21 else '2'
        print(f'Hand final status: {player_hand}')

    def play(self, bet=50, n_rounds=1):
        for i in range(n_rounds):
            self.__player_bank -= bet
            self._pot += bet
            dealer_hand = Hand()
            self.deal_to(dealer_hand, 2)
            player_hands = [Hand()]
            self.deal_to(player_hands[0], 2)
            for hand in player_hands:
                self.play_hand(hand, dealer_hand, bet, player_hands)


game_deck = Deck(shuffled=True, n_decks=8)
my_game = Game(game_deck, 10000)
my_game.play()
