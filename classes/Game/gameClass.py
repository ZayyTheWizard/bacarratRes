from typing import Tuple
from classes.Player.playerClass import playerClass
from random import randrange

class game:
    def __init__(self, player: playerClass):
        # User Defined Variables
        self.player: playerClass = player

        # Utility varibles
        self.totalMap: dict = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 0,
            11: 1,
            12: 2,
            13: 3,
            14: 4,
            15: 5,
            16: 6,
            17: 7,
            18: 8,
            19: 9
        }
        
    def trueTotal(self, num: int):
        return self.trueTotal[num]
    
    def playRound(self, bets: Tuple[int, int, int]) -> Tuple[bool, bool, bool]:
        '''
        Plays a round of bacarrat -1: No Bet, 0: Tie, 1: Player Win, 2: Banker Wins
        '''

        # First Draw first card player 

        # Draw for banker

        # Draw second card Player
        # Determine if player needs third card <= 5

        # Draw third card for banker


        # If PlayerThird card draw third card
        # Draw player card
        # Determine if Banker needs thirs car.

        # If banker third card
        # Draw banker third card

        # If player total and Banker total equal
        # return (0, 0, 1) (player, banker, tie)

        # If player total > Banker
        # return (1, 0, 0) (player, banker, tie)

        # If Player total < Banker
        # return (0, 1, 0) (player, banker, tie)
        pass