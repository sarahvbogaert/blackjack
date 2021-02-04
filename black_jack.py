from card_game import Deck
from player import Player, Dealer


class BlackJack:

    def __init__(self, name, balance, bet):
        self.player = Player(name, balance)
        self.dealer = Dealer()
        self.deck = Deck()
        self.bet = bet

    def game(self):
        """
        Several rounds of player and dealer playing one after another
        """
        self.deck.shuffle()
        while True:
            enough_balance = self.player.pay(self.bet)  # check if balance high enough
            if not enough_balance:
                break
            sum_player, burst_player = self.player.play(self.deck)
            if burst_player:
                print(f"Player {self.player.name} Looses!")
            else:
                sum_dealer, burst_dealer = self.dealer.play(self.deck)
                if sum_player > sum_dealer or burst_dealer:
                    print(f"Player {self.player.name} Wins!")
                    self.player.win(2*self.bet)
                elif sum_player == sum_dealer:
                    print(f"Nobody Wins!")
                    self.player.win(self.bet)
                else:
                    print(f"Player {self.player.name} Looses!")
            print(self.player)
            if not self.game_on():  # asks user if he wants to continue playing
                break

    @staticmethod
    def game_on():
        """
        Asks user if he wants to continue playing
        :return: True or False
        """
        while True:
            cont = input(f"Do you want to continue playing? (Y or N): ")
            if cont not in ['Y', 'N']:
                print("Wrong input. Please try again.")
                continue
            break
        return cont == "Y"


if __name__ == "__main__":
    bj = BlackJack('Sarah', 100, 20)
    bj.game()
