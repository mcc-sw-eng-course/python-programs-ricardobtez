# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: TicTacToe game

from random import randrange
from copy import deepcopy
from game import *
from IPlayer import enUser

class enMarker(IntEnum):
    EMPTY = auto()
    X = auto()
    O = auto()

    def __str__(self):
        returnValue = self.name if enMarker.EMPTY != self.value else ' '
        return str(returnValue)

class TicTacToe(IGame):
    def __init__(self, boTwoPlayers: bool = False):
        self.gamesPlayed = 0
        self.boTwoPlayers = boTwoPlayers
        self.openPositions = 9
        self.board.setBoardInfo(3, [enMarker.EMPTY, enMarker.X, enMarker.O], enBoardType.TIC_TAC_TOE)
        self.gameScore = {
            "PLAYER_ONE": 0,
            "COMPUTER": 0,
            "PLAYER_TWO": 0,
            "tie": 0
        }

        if(True == self.boTwoPlayers):
            self.turn = (enUser)(randrange(1, enUser.INVALID_USER, 1))
        else:
            self.turn = (enUser)(randrange(0, ((int)enUser.INVALID_USER) - 1, 1))

    def newGame(self):
        self.board.resetBoard()
        self.openPositions = 9

    # While loop with the logic of the game
    def play(self):
        boGameFinished = False
        winner = enUser.INVALID_USER
        self.gamesPlayed += 1

        while (False == boGameFinished):
            posTuple = (-1,-1)

            if (enUser.COMPUTER == self.turn):
                posTuple = self.__getComputerMove()
                self.board[ posTuple[0] ][ posTuple[1] ] = enMarker.X
                boGameFinished = self.__boPlayerWon(posTuple[0], posTuple[1])
                winner = self.turn if (boGameFinished) else winner
                self.turn = enUser.PLAYER_ONE
            else:
                posTuple = self.__getUserMove(self.turn)
                self.board[ posTuple[0] ][ posTuple[1] ] = enMarker.O
                boGameFinished = self.__boPlayerWon(posTuple[0], posTuple[1])
                winner = self.turn if (boGameFinished) else winner

                if (True != self.boTwoPlayers):
                    self.turn = enUser.COMPUTER
                else:
                    self.turn = enUser.PLAYER_TWO if (self.turn == enUser.PLAYER_ONE) else enUser.PLAYER_ONE

            self.openPositions -= 1
            # Verification of the game finished
            if (0 == self.openPositions):
                boGameFinished = True
            # End verification of game finished
        if (winner != enUser.INVALID_USER):
            print("Game finished! the winner is:{}".format(str(winner)))
            self.gameScore[str(winner)] += 1
        else:
            print("It was a sad TIE")
            self.gameScore["tie"] += 1
    def importGame(self, fileName: str):
        # Creates empty board to be later filled
        board = [[enMarker.EMPTY for x in range(3)] for y in range(3)]
        fileHdlr = open(fileName, 'r')
        yIndex = 0
        for line in fileHdlr:
            if(line[0] != '-'):
                lineList = line.strip().split('|')
                for xIndex in range(len(lineList)):
                    if ('X' == lineList[xIndex]):
                        board[yIndex][xIndex] = enMarker.X
                    elif('O' == lineList[xIndex]):
                        board[yIndex][xIndex] = enMarker.O
                yIndex += 1
        fileHdlr.close()
        self.board = deepcopy(board)

    # Get games data
    def getGamesReport(self):
        print("The number of games played was:" + str(self.gamesPlayed))
        print("The amount of games won by {} was: {}".format(
            str(enUser.PLAYER_ONE), self.gameScore["PLAYER_ONE"]))
        print("The number of ties is:{}".format( str(self.gameScore["tie"]) ))
        print("The number of times won by the {} was:{}".format(
            str(enUser.COMPUTER), self.gameScore["COMPUTER"]))

    def __boCheckHorRow(self, row: int):
        boReturn = True
        cellValue = enMarker.EMPTY
        if ((3 > row) and (0 <= row)):
            for x in range(3):
                if (enMarker.EMPTY == self.board[row][x]):
                    boReturn = False
                    break
                if (enMarker.EMPTY == cellValue):
                    cellValue = self.board[row][x]
                if (cellValue != self.board[row][x]):
                    boReturn = False
                    break
        else:
            raise ValueError
        return boReturn

    def __boCheckVerCol(self, col: int):
        boReturn = True
        cellValue = enMarker.EMPTY
        if ((3 > col) and (0 <= col)):
            for y in range(3):
                if (enMarker.EMPTY == self.board[y][col]):
                    boReturn = False
                    break
                if (enMarker.EMPTY == cellValue):
                    cellValue = self.board[y][col]
                if (cellValue != self.board[y][col]):
                    boReturn = False
                    break
        else:
            raise ValueError
        return boReturn

    def __boCheckDiag(self, startUpper: bool):
        boReturn = True
        cellValue = enMarker.EMPTY
        y = 0
        if (False == startUpper):
            y = 2
        for x in range(3):
            if (enMarker.EMPTY == self.board[y][x]):
                boReturn = False
                break
            if (enMarker.EMPTY == cellValue):
                cellValue = self.board[y][x]
            if (cellValue != self.board[y][x]):
                boReturn = False
                break
            if(True == startUpper):
                y += 1
            else:
                y -= 1 
        return boReturn

    def __boPlayerWon(self, y, x):
        boReturn = False

        if ((x != 1) and (y != 1)):
            if (x == y):
                boReturn = self.__boCheckDiag(True)
            else:
                boReturn = self.__boCheckDiag(False)

        if (True != boReturn):
            boReturn = self.__boCheckHorRow(y)
        if (True != boReturn):
            boReturn = self.__boCheckVerCol(x)
        # Checks both the diagonals in cas of the 1 1 position
        if((y == 1) and (x == 1) and (True != boReturn)):
            boReturn = self.__boCheckDiag(True)
            if(True != boReturn):
                boReturn = self.__boCheckDiag(False)

        return boReturn

if __name__ == '__main__':
    print('Wellcome to the TicTacToe game')
    rand = randrange(0,2,1)
    game = TicTacToe()
    for i in range(3):
        game.newGame()
        game.play()

    game.getGamesReport()
