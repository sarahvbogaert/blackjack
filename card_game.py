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



