import random


class Card:
    """
    A card from a deck
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Deck.values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    A deck of cards
    """
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
             'Jack', 'Queen', 'King', 'Ace']
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}

    def __init__(self):
        self.all_cards = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.all_cards.append(Card(suit, rank))

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, cards):
        self.all_cards.extend(cards)

# static functions ---------------------------------------------------


def is_there_burst(final_sums):
    """
    returns true if there is a burst
    :param final_sums: list of possible sums (in increasing order)
    :return: true if burst
    """
    if final_sums[0] > 21:
        print("BURST!")
        return True
    return False

# ---------------------------------------------------------------------------------------------


class Person:
    """
    A player for a card game
    """
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self, cards):
        if isinstance(cards, list):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def clear_cards(self):
        self.all_cards = []

    def print_cards(self):
        print(f"Actual cards of player {self.name}: ")
        for c in self.all_cards:
            print(c)

    def sum_cards(self):
        sum_c = 0
        num_aces = 0
        for c in self.all_cards:
            sum_c += c.value
            if c.rank == "Ace":
                num_aces += 1
        final_sums = [sum_c]
        for i in range(num_aces):
            sum_c += 10
            final_sums.append(sum_c)
        return final_sums

    def play(self, deck):
        """
        play one time
        :param deck:
        :return: final_sums (list), burst (bool)
        """
        final_sums = None
        print(f"Player {self.name} gets two cards.")
        self.add_cards([deck.deal_one(), deck.deal_one()])
        self.print_cards()
        burst = False
        while True:
            h_or_s = self.hit_or_stand(final_sums)
            if h_or_s == "H":
                print("HIT!")
                self.add_cards(deck.deal_one())
                self.print_cards()
                final_sums = self.sum_cards()
                if is_there_burst(final_sums):
                    burst = True
                    break
            else:
                print("STAND!")
                break
        if final_sums is None:  # if player never hit
            final_sums = self.sum_cards()
        deck.add_cards(self.all_cards)
        self.clear_cards()
        return final_sums, burst

    def hit_or_stand(self, final_sums):
        raise NotImplementedError("This function should not be called in abstract class.")

# ---------------------------------------------------------------------------------------------------


class Player(Person):
    def __init__(self, name, balance):
        Person.__init__(self, name)
        self.balance = balance

    def __str__(self):
        return f"Player {self.name} has a balance of ${self.balance}."

    def pay(self, amount):
        """
        if amount > balance, return False; otherwise, decrease balance and return True
        :param amount: to remove from balance
        :return:
        """
        if amount > self.balance:
            print(f"Not enough balance! Only ${self.balance} left.")
            return False
        self.balance -= amount
        return True

    def win(self, amount):
        self.balance += amount

    def hit_or_stand(self, _):
        """
        asks the player if he wants to hit or stand
        :return: either "H" (hit) or "S" (stand)
        """
        while True:
            move = input("Do you want to hit or stand? (H or S): ")
            if move not in ['H', 'S']:
                print("Wrong input. Please try again.")
                continue
            break
        return move

# ---------------------------------------------------------------------------------------------------


class Dealer(Person):
    def __init__(self):
        Person.__init__(self, "Dealer")

    def hit_or_stand(self, final_sums):
        """
        if burst, stand. otherwise, if sum is 17 or higher and <= 21, stand, except if sum is a soft 17.
        in other cases, hit.
        :param final_sums:
        :return:
        """
        if final_sums is None:
            final_sums = self.sum_cards()
        if final_sums[0] > 21:  # should not happen
            print("BURST!")
            return "S"
        highest_smaller_21 = final_sums[0]
        index = 1
        while index < len(final_sums) and final_sums[index] <= 21 :
            highest_smaller_21 = final_sums[index]
            index += 1
        index -= 1  # index of chosen sum in final_sums
        if highest_smaller_21 < 17 or (highest_smaller_21 == 17 and index >= 1):  # smaller than 17 or soft 17
            return "H"
        else:
            return "S"

# ---------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    bj_deck = Deck()
    bj_deck.shuffle()
    player = Player("Sarah", 100)
    player.play(bj_deck)


