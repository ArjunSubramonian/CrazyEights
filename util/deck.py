from util.card import Card, Rank, Suit, Color
from random import shuffle, randrange

class Deck:
    def __init__(self, exclude_jokers=False):
        self.create_shuffled_deck(exclude_jokers)

    def create_shuffled_deck(self, exclude_jokers):
        self.deck = []
        for rank in Rank:
            if rank == Rank.JOKER:
                continue
            for suit in Suit:
                color = Color.BLACK
                if suit == Suit.HEARTS or suit == Suit.DIAMONDS:
                    color = Color.RED
                self.deck.append(Card(rank, suit, color))

        if not exclude_jokers:
            self.deck.append(Card(Rank.JOKER, None, None))

        shuffle(self.deck)

    def draw(self, n):
        if len(self.deck) >= n:
            cards = self.deck[-n:]
            self.deck = self.deck[:-n]
            return cards
        return []

    def insert_randomly(self, card):
        self.deck.insert(randrange(len(self.deck) + 1), card)

    def shuffle(self):
        shuffle(self.deck)



