import sys
from util.player import Player
from util.deck import Deck
from util.card import Rank
from random import choice

class Game:
    def __init__(self):
        self.print_break(3)
        self.players, self.deck = self.prep()
        self.print_break(3)
        self.dealer, self.faceup = self.deal(self.players, self.deck)

    def print_break(self, n):
        [print() for i in range(n)]

    def prep(self):
        ready = input('Ready to play crazy eights (y/n)? ').lower()
        if ready != 'y' and ready != 'yes':
            sys.exit(0)

        self.print_break(2)

        print('Awesome!')
        num_players = input('Enter the number of players (2-8): ').strip()
        while not num_players.isdigit() or (num_players.isdigit() and (int(num_players) < 2 or int(num_players) > 8)):
            num_players = input('Enter a valid number of players (2-8): ').strip()
        num_players = int(num_players)

        players = []
        for p in range(1, num_players + 1):
            player = input('Enter the name of Player ' + str(p) + ': ').strip()
            while player == '':
                player = input('Please enter a valid name for Player ' + str(p) + ': ').strip()
            players.append(Player(player))
        deck = Deck(exclude_jokers=True)

        return players, deck

    def deal(self, players, deck):
        dealer = choice(players)
        input(dealer.name + ' is the dealer! Press enter to deal 5 cards to each player.')
        for t in range(5):
            for player in players:
                player.take_cards(deck.draw(1))
        faceup = deck.draw(1)[0]
        while faceup.rank == Rank.EIGHT:
            deck.insert_randomly(faceup)
            faceup = deck.draw(1)[0]
        faceup = [faceup]
        print('Cards have been dealt, and faceup pile has been created.')
        return dealer, faceup

    def format_cards(self, cards):
        cards_output = '\n'
        for idx, card in enumerate(cards):
            cards_output += str(idx + 1) + ' ' + str(card) + '\n'
        return cards_output

    def play(self):
        self.print_break(4)
        i = 0
        n = len(self.players)
        while True:
            current_player = self.players[i % n]
            self.print_break(2)
            input('Ready ' + current_player.name + '? Press enter to proceed...')
            self.print_break(2)
            print('The top faceup card is: ' + str(self.faceup[-1]))
            self.print_break(2)
            print('Your cards are: ' + self.format_cards(current_player.hand))
            self.print_break(2)

            unable_to_play = True
            for card in current_player.hand:
                if self.is_valid_card(card):
                    unable_to_play = False

            if not unable_to_play:
                card_idx = input('Enter the index of the card you want to play (1-' + str(len(current_player.hand)) + '): ').strip()
                not_valid_num = not card_idx.isdigit() or (card_idx.isdigit() and (int(card_idx) < 1 or int(card_idx) > len(current_player.hand)))
                valid_card = card_idx.isdigit() and (int(card_idx) >= 1 and int(card_idx) <= len(current_player.hand)) and self.is_valid_card(current_player.hand[int(card_idx) - 1])
                while not_valid_num or not valid_card:
                    if not_valid_num:
                        card_idx = input('Please enter a valid number between 1 and ' + str(len(current_player.hand)) + ': ')
                    elif not valid_card:
                        card_idx = input('Please play an 8 or a card of the same denomination or suit as the top faceup card: ')
                    not_valid_num = not card_idx.isdigit() or (card_idx.isdigit() and (int(card_idx) < 1 or int(card_idx) > len(current_player.hand)))
                    valid_card = card_idx.isdigit() and (int(card_idx) >= 1 and int(card_idx) <= len(current_player.hand)) and self.is_valid_card(current_player.hand[int(card_idx) - 1])
                card_idx = int(card_idx)
                card = current_player.hand.pop(card_idx - 1)
                self.faceup.append(card)
            else:
                print('Oof, you have no card you can play! Drawing cards until one works...')
                while len(self.deck.deck) > 0:
                    card = self.deck.draw(1)[0]
                    print('Drew ' + str(card))
                    if self.is_valid_card(card):
                        print(str(card) + ' works!')
                        self.faceup.append(card)
                        break
                    else:
                        print(str(card) + ' doesn\'t work :(')
                        current_player.take_cards([card])
                if len(self.deck.deck) == 0:
                    self.deck.deck = self.faceup[:-1]
                    self.faceup = [self.faceup[-1]]
                    self.deck.shuffle()

            if len(current_player.hand) == 0:
                self.print_break(2)
                print('Game has ended! ' + current_player.name + ' is the winner.')
                self.print_break(2)
                return current_player

            i += 1

    def is_valid_card(self, card):
        return card.rank == Rank.EIGHT or card.suit == self.faceup[-1].suit or card.rank == self.faceup[-1].rank






















