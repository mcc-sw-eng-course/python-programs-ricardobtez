# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: Checkers class

import sys
sys.path.append('../L8Exercises/src')
from game import *
from display import Display
from enum import auto, IntEnum
from playerMgr import *

class enChecker(IntEnum):
    EMPTY = auto()
    RED = auto()
    WHITE = auto()

    def __str__(self):
        returnValue = ' '
        if (enChecker.RED == self.value):
            returnValue = 'R'
        elif (enChecker.WHITE == self.value):
            returnValue = 'W'
        return returnValue

class Checkers(IGame):
    def __init__(self, boTwoPlayers:bool=False):
        self.boTwoPlayers = boTwoPlayers
        self.displayMgr = Display.getInstance()
        self.board = Board()
        self.board.setBoardInfo(8, [enChecker.EMPTY, enChecker.RED, enChecker.WHITE], enBoardType.CHECKERS)
        self.gameScore = {
            "PLAYER_ONE": 0,
            "COMPUTER": 0,
            "PLAYER_TWO": 0,
            "tie": 0
        }
        if(True == self.boTwoPlayers):
            playerList = [enUser.PLAYER_ONE, enUser.PLAYER_TWO]
        else:
            playerList = [enUser.COMPUTER, enUser.PLAYER_ONE]
        self.playerMgr = PlayerMgr(playerList, [enChecker.WHITE, enChecker.RED])

    def newGame(self):
        self.board.resetBoard()
        self.__resetBoard()

    def play(self):
        self.displayMgr.display(str(self.board))
        boGameFinished = False
        winner = enUser.INVALID_USER

        while (False == boGameFinished):
            self.playerMgr.getNextMove(self.board)
            self.playerMgr.nextPlayer()
            self.playerMgr.getNextMove(self.board)
            boGameFinished = True


    def __resetBoard(self):
        # Fills the board with the corresponding values in the dark positions
        for row in range(8):
            for column in range(8):
                # Even positions
                if ((column % 2) == 0):
                    if ((row % 2) != 0):
                        if (row < 3):
                            self.board.boFillPosition(enChecker.WHITE, row, column)
                        elif (row > 4):
                            self.board.boFillPosition(enChecker.RED, row, column)
                        else:
                            continue
                # Odd positions
                else:
                    if ((row % 2) != 0):
                        if (row < 4):
                            # pass
                            self.board.boFillPosition(enChecker.WHITE, row-1, column)
                        elif (row > 5):
                            self.board.boFillPosition(enChecker.RED, row-1, column)
                        else:
                            continue



if __name__ == '__main__':
    checkers = Checkers()
    checkers.newGame()
    checkers.play()
