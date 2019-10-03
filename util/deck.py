from card import Card, Rank, Suit, Color
from random import shuffle

class Deck:
    def __init__(self, exclude_jokers=False):
        self.create_shuffled_deck(exclude_jokers)

    def create_shuffled_deck(self, exclude_jokers):
        self.deck = []
        for rank in Rank:
            for suit in Suit:
                alt_value = rank
                if rank == Rank.KING or rank == Rank.QUEEN or rank == Rank.JACK:
                    alt_value = 10
                color = Color.BLACK
                if suit == Suit.HEARTS or suit == Suit.DIAMONDS:
                    color = Color.RED
                self.deck.append(Card(rank, suit, color, alt_value=alt_value))

        if not exclude_jokers:
            self.deck.append(Card(Rank.JOKER, None, None))

        shuffle(self.deck)

    def draw(n):
        if len(self.deck) >= n:
            cards = self.deck[-n:]
            self.deck = self.deck[:-n]
            return cards
        return []



