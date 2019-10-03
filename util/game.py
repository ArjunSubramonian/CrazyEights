import sys
from util.player import Player
from util.deck import Deck

class Game:
    def __init__():
        print_break(3)
        self.players, self.deck = prep()
        print_break(3)
        self.dealer, self.discard = deal(players, deck)

    def print_break(n):
        [print() for i in range(n)]

    def prep():
        ready = input('Ready to play gin rummy (y/n)? ').lower()
        if ready != 'y' and ready != 'yes':
            sys.exit(0)

        print_break(2)

        print('Awesome!')
        num_players = 2
        players = []
        for p in range(1, num_players + 1):
            player = input('Enter the name of Player ' + str(p) + ': ').strip()
            while player == '':
                player = input('Please enter a valid name for Player ' + str(p) + ': ').strip()
            players.append(Player(player))
        deck = Deck(exclude_jokers=True)

        return players, deck

    def deal(players, deck):
        dealer = random.choice(players)
        input(dealer.name + ' is the dealer! Press enter to deal 10 cards to each player.')
        for t in range(10):
            for player in players:
                player.take_cards(deck.draw(1))
        discard = [deck.draw(1)]
        print('Cards have been dealt, and discard pile has been created.')
        return dealer, discard

    def format_cards(cards):
        cards_output = ''
        for idx, card in enumerate(cards):
            cards_output += str(idx + 1) + ' ' + card
        return cards_output

    def play():
        print_break(4)
        i = 0
        n = len(self.players)
        while True:
            current_player = self.players[i % n]
            print_break(2)
            input('Ready ' + current_player.name + '? Press enter to proceed...')
            print_break(2)
            print('The top discard card is: ' + self.discard[-1])
            print_break(2)
            print('Your cards are: ' + format_cards(current_player.hand))
            print_break(2)

            decision = input('Do you want to take the top card from the draw (dr) pile or the discard (di) pile (dr/di)?').strip()
            while decision != 'dr' and decision != 'di':
                decision = input('Please enter either dr or di!')
            if decision == 'dr':
                current_player.take_cards(self.deck.draw(1))
            else:
                current_player.take_cards(self.discard.pop())

            print_break(2)
            print('Your cards are now: ' + format_cards(current_player.hand))
            print_break(2)
            print('Do you want to knock?')


            card_idx = input('Enter the index of the card you want to discard (1-10): ')
            while card_idx < 1 or card_idx > 10:
                card_idx = input('Please enter a number between 1 and 10!')
            card = current_player.hand.pop(card_idx - 1)
            self.deck.append(card)

            if len(self.deck) <= 2:
                print('Game has ended in a draw!')
                return None

            i += 1






















