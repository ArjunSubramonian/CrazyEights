from enum import Enum 

class Rank(Enum):
    JOKER = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    DEUCE = 2
    ACE = 1

class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

class Color(Enum):
    BLACK = 1
    RED = 2

class Card:
    def __init__(self, rank, suit, color, alt_value=None):
        self.rank = rank
        if alt_value:
            self.value = alt_value
        else:
            self.value = self.rank
        self.suit = suit
        self.color = color

    def __str__(self):
        return self.rank.name + ' OF ' + self.suit.name