from typing import List, Tuple
from classes.Game.gameClass import game

class playerClass:
    def __init__(self, strategy: List[(int, int, int)], minBet: int, startingCash: int, shoeReset: bool = False, betMinTuple: Tuple[int, int, int] = (0, 0, 0),):
        '''
        Bets tuple are as follows (Player, Banker, Tie)
        '''
        ## user defined varibles
        self.strategy: List[(int, int, int)] = strategy
        self.Cash: int = startingCash
        self.shoeReset: bool = shoeReset
        self.currBetTuple: Tuple[int, int, int] = betMinTuple
        self.minBet = minBet

        ## utilty variables
        self.winCount: int = 0
        self.loseCount: int = 0
        self.ties: int = 0
        self.highestCashReached: int = 0
        self.highestCashRoundReached: int = 0
        self.currentRound: int = 0
        self.strategyOfI: int = 0
        self.initBetTuple: Tuple[int, int, int] = betMinTuple
 
    def incrementWin(self) -> None:
        '''
        Increments Win count
        '''
        self.winCount+=1
    def incrementLose(self) -> None:
        '''
        Increments Lose Count
        '''
        self.loseCount+=1
    def incrementTie(self) -> None:
        '''
        Increments Tie Count
        '''
        self.ties+=1
    def updateHighestCash(self) -> None:
        '''
        Update Highest Cash and the round we reached it
        '''
        if self.Cash > self.highestCashReached:
            self.highestCashReached = self.Cash
            self.highestCashRoundReached = self.currentRound
    def incrementCurrRound(self) -> None:
        '''
        Increment Current Round
        '''
        self.currentRound+=1

    def makeBet(self, winOrLose: Tuple[bool, bool, bool]) -> None:
        '''
        keep track of cash and betting amount
        '''

        # [Player, Banker, Tie]
        self.Cash -= sum(self.currBetTuple)

        if winOrLose:
            ## Handle win condition
            if winOrLose[0] == True:
                # Bet on player was a win 1:1
                self.Cash += self.currBet*2
                self.currBetTuple[0] = self.initBetTuple[0]
                self.strategyOfI = 0
            if winOrLose[1] == True:
                # Bet on Banker was a win 1:0.95
                self.Cash += self.currBet*1.95
                self.currBetTuple[1] = self.initBetTuple[1] 
                self.strategyOfI = 0
            if winOrLose[2] == True:
                # Bet on tie was a win 1:9
                self.cash += self.currBet*9
                self.currBetTuple[2] = self.initBetTuple[2]


            # A lost bet if tie false doesn't matter
            if winOrLose[0] == False:
                # Bet on player was a win 1:1
                self.currBetTuple[0] = self.currBetTuple[0]*2
                self.strategyOfI += 1
            if winOrLose[1] == False:
                # Bet on Banker was a win 1:0.95
                self.currBetTuple[1] = self.currBetTuple[1]*2 
                self.strategyOfI += 1