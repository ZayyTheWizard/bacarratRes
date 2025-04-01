from classes.Game.gameClass import game
from classes.Player.playerClass import playerClass
import numpy

if __name__ == '__main__':
    numpy.seterr(divide='ignore', invalid='ignore')
    player = playerClass([(1,0,0),(1,0,0),(1,0,0)], 10, 100, [10,0,0])
    gameOb = game(player=player)

    while player.Cash > 0:
        print(f"before bet {player.Cash}")
        gameOb.playRound()
        print(f"after bet {player.Cash}")
