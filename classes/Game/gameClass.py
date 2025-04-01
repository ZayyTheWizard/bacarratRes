from typing import List
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
            19: 9,
            20: 0,
            21: 1,
            22: 2,
            23: 3,
            24: 4,
            25: 5,
            26: 6,
            27: 7,
            28: 8,
            29: 9,
            30: 0,
        }
        
        self.cardTotals: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0]
    def trueTotal(self, num: int):
        return self.trueTotal[num]
    
    def playRound(self) -> None:
        '''
        Plays a round of bacarrat.
        '''
        self.playerDrawThird: bool = False
        self.playerThirdCard: int
        self.playerTotal: int

        self.bankerDrawThird: bool = False
        self.bankerThirdCard: int
        self.bankerTotal: int

        # First Draw first card player
        self.playerFirstCard: int = self.cardTotals[randrange(0, 12)] # between 0 and 12

        # Draw for banker
        self.bankerFirstCard: int = self.cardTotals[randrange(0, 12)] # between 0 and 12

        # Draw second card Player
        self.playerSecondCard: int = self.cardTotals[randrange(0, 12)] # between 0 and 12

          # Draw second card for banker
        self.bankerSecondCard: int = self.cardTotals[randrange(0, 12)] # between 0 and 12

        self.playerTotal = self.totalMap[self.playerFirstCard + self.playerSecondCard]
        self.bankerTotal = self.totalMap[self.bankerFirstCard + self.bankerSecondCard]

        # Determine if player needs third card <= 5
        if (self.totalMap[self.playerFirstCard + self.playerSecondCard] <= 5):
            self.playerDrawThird = True

        # If PlayerThird card draw third card
        if self.playerDrawThird == True:
            self.playerThirdCard: int = self.cardTotals[randrange(0, 12)] # between 0 and 12
            self.playerTotal = self.totalMap[self.playerFirstCard + self.playerSecondCard + self.playerThirdCard]

        # Determine if Banker needs thirs car.
        match (self.bankerTotal):
            case 0:
                self.bankerDrawThird = True
            case 1: 
                self.bankerDrawThird = True
            case 2: 
                self.bankerDrawThird = True
            case 3:
                if self.playerDrawThird and self.playerThirdCard != 8 and self.playerThirdCard != 9:
                    self.bankerDrawThird = True
            case 4:
                if self.playerDrawThird and (self.playerThirdCard >= 2 or self.playerThirdCard <= 7):
                    self.bankerDrawThird = True
            case 5:
                if self.playerDrawThird and (self.playerThirdCard >= 4 or self.playerThirdCard <= 7):
                    self.bankerDrawThird = True
            case 6:
                if self.playerDrawThird and (self.playerThirdCard >= 6 or self.playerThirdCard <= 7):
                    self.bankerDrawThird = True
            case 7:
                self.bankerDrawThird = False
            case 8:
                self.bankerDrawThird = False
                if self.playerTotal != 8 and self.bankerTotal == 8:
                    self.player.makeBet((0,1,0))
                    return
            case 9:
                self.bankerDrawThird = False
                if self.playerTotal != 9 and self.bankerTotal == 9:
                    self.player.makeBet((0,1,0))
                    return
            case _:
                print(f"Invalid Value {self.bankerTotal}")
        # If banker third card
        if(self.bankerDrawThird):
            self.bankerThirdCard = self.cardTotals[randrange(0, 12)]
            self.bankerTotal = self.totalMap[self.bankerFirstCard + self.bankerSecondCard + self.bankerThirdCard]


        # If player total and Banker total equal
        # return (0, 0, 1) (player, banker, tie)
        if self.playerTotal == self.bankerTotal:
            self.player.makeBet((0,0,1))

        # If player total > Banker
        # return (1, 0, 0) (player, banker, tie)
        if self.playerTotal > self.bankerTotal:
            self.player.makeBet((1,0,0))

        # If Player total < Banker
        # return (0, 1, 0) (player, banker, tie)
        if self.playerTotal < self.bankerTotal:
            self.player.makeBet((0,1,0))