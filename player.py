class Person:
    """
    A player/dealer for black jack card game
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
        """
        :return: a list of all possible sums of the person's cards (depending if ace has value 1 or 11)
                 in increasing order
        """
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
        :param deck: deck of cards used for playing
        :return: final_sums (list of possible sums of the cards received), burst (boolean)
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
                if final_sums[0] > 21:
                    print("BURST!")
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
    """
    A player is a person playing blackjack with a balance
    """
    def __init__(self, name, balance):
        Person.__init__(self, name)
        self.balance = balance

    def __str__(self):
        return f"Player {self.name} has a balance of ${self.balance}."

    def pay(self, amount):
        """
        decrease player's balance by amount (if balance sufficient)
        :param amount: to remove from balance
        :return: True if player has enough balance, False otherwise
        """
        if amount > self.balance:
            print(f"Not enough balance! Only ${self.balance} left.")
            return False
        self.balance -= amount
        return True

    def win(self, amount):
        """
        increase player's balance with amount
        """
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
    """
    The dealer is the person dealing the cards to the black jack players
    """
    def __init__(self):
        Person.__init__(self, "Dealer")

    def hit_or_stand(self, final_sums):
        """
        The dealer does not decide himself if he hits or stands. His behavior is deterministic and depends
        on the cards he has received until now.
        if burst, stand. otherwise, if sum is 17 or higher and <= 21, stand, except if sum is a soft 17.
        in other cases, hit.
        :param final_sums: possible sums of the cards he already owns
        :return: "H" or "S"
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
