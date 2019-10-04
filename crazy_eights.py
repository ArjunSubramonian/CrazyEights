from util.game import Game

'''Rules:
https://bicyclecards.com/article/top-three-classic-family-card-games/'''

if __name__ == '__main__':
    while True:
        g = Game()
        winner = g.play()
        again = input('Would you like to play again (y/n)? ')
        if not again:
            break