from blackjack_dealer import BlackJackDealer
from blackjack_hand import BlackJackHand
from blackjack_player import BlackJackPlayer


class IOManager:

    def show_dealer_hand_to_user(self, hand: BlackJackHand, upcard_only=True):
        if len(hand) == 2 and upcard_only:
            hidden_hand_string = f'[X,{hand.cards[1]}]'
            print('Dealer Hand: ', hidden_hand_string)
        else:
            print('Dealer Hand: ', str(hand))

    def show_hand_to_user(self, hand: BlackJackHand, pre_text=''):
        print(pre_text, str(hand))

    def show_financial_stats_to_user(self, player: BlackJackPlayer, hand: BlackJackHand):
        print(f'Bank: {player.bank}$\t Bet Size: {hand.bet_size}$')

    def show_player_options(self, hand: BlackJackHand):
        print('1.Hit\n2.Stand')
        if hand.can_split():
            print('3.Split')
        if len(hand) == 2:
            print('4.Double Down')

    def print_turn_status(self, player: BlackJackPlayer, hand: BlackJackHand, dealer: BlackJackDealer):
        self.show_dealer_hand_to_user(dealer.hand)
        self.show_hand_to_user(hand, pre_text='Player Hand: ')
        self.show_financial_stats_to_user(player, hand)

    def get_player_bet(self):
        bet = input('How much would you like to bet?')
        return int(bet)

    def get_player_choice(self):
        return int(input())

    def print_end_turn_message(self, hand: BlackJackHand):
        print('Turn ended with hand:', str(hand))

    def print_blackjack_message(self):
        print('******************')
        print('*   BLACKJACK!   *')
        print('******************')

    def print_winnings_to_player(self, winnings_sum: int, winnings_status: str):
        print(winnings_status)
        print(f'You won {winnings_sum}$')
