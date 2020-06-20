from blackjack_hand import BlackJackHand
from blackjack_player import BlackJackPlayer


class IOManager:

    def show_dealer_hand_to_user(self, hand: BlackJackHand):
        if len(hand) == 2:
            hidden_hand_string = f'[X,{hand.cards[1]}'
            print(hidden_hand_string)
        else:
            self.show_hand_to_user(hand)

    def show_hand_to_user(self, hand: BlackJackHand):
        print(str(hand))

    def show_financial_stats_to_user(self, player: BlackJackPlayer, hand: BlackJackHand):
        print(f'Bank: {player.bank}\t Bet Size: {hand.bet_size}')

    def show_player_options(self, hand: BlackJackHand):
        print('1.Hit\n2.Stand')
        if hand.can_split():
            print('3.Split')
        if len(hand) == 2:
            print('4.Double Down')

    def print_turn_status(self, player: BlackJackPlayer, hand: BlackJackHand, dealer: BlackJackDealer):
        self.show_dealer_hand_to_user(dealer.hand)
        self.show_hand_to_user(hand)
        self.show_financial_stats_to_user(player, hand)
        self.show_player_options(hand)

    def get_player_bet(self):
        bet = input('How much would you like to bet?')
        return int(bet)

    def get_player_choice(self):
        return int(input())
