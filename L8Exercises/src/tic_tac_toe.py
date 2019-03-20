# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: TicTacToe game

from random import randrange
from enum import Enum, auto, IntEnum
from copy import deepcopy

class enUser(Enum):
    COMPUTER = auto()
    PLAYER_ONE = auto()
    PLAYER_TWO = auto()
    INVALID_USER = auto()

    def __str__(self):
        return str(self.name)

class enMarker(IntEnum):
    EMPTY = auto()
    X = auto()
    O = auto()

    def __str__(self):
        returnValue = self.name if enMarker.EMPTY != self.value else ' '
        return str(returnValue)

class TicTacToe:
    def __init__(self, startUser: enUser = enUser.COMPUTER):
        self.enStartUser = startUser
        self.board = [[enMarker.EMPTY for x in range(3)] for y in range(3)]
        self.gamesPlayed = 0
        self.difficulty = 1
        # Tupple with (Player1, Computer/Player2, Tie) score
        self.gameScore = (0,0,0)
        self.turn = enUser.COMPUTER
        self.openPositions = 9

    def newGame(self):
        self.board = [[enMarker.EMPTY for x in range(3)] for y in range(3)]
        self.openPositions = 9
    def display(self):
        for row in range(len(self.board)):
            rowStr = ''
            if (row > 0):
                print(5*'-')
            for column in range(len(self.board[row])):
                if(column > 0):
                    rowStr += '|'
                rowStr += str(self.board[row][column])
            print(rowStr)

    # While loop with the logic of the game
    def play(self):
        boGameFinished = False
        winner = enUser.INVALID_USER

        while (False == boGameFinished):
            posTuple = (-1,-1)

            if (enUser.COMPUTER == self.turn):
                posTuple = self.__getComputerMove()
                self.board[ posTuple[0] ][ posTuple[1] ] = enMarker.X
                boGameFinished = self.__boPlayerWon(posTuple[0], posTuple[1])
                winner = self.turn if (boGameFinished) else winner
                self.turn = enUser.PLAYER_ONE
            elif (enUser.PLAYER_ONE == self.turn):
                posTuple = self.__getUserMove(self.turn)
                self.board[ posTuple[0] ][ posTuple[1] ] = enMarker.O
                boGameFinished = self.__boPlayerWon(posTuple[0], posTuple[1])
                winner = self.turn if (boGameFinished) else winner
                self.turn = enUser.COMPUTER

            self.openPositions -= 1
            # Verification of the game finished
            if (0 == self.openPositions):
                boGameFinished = True
            # End verification of game finished
        if (enUser != enUser.INVALID_USER):
            print("Game finished! the winner is:{}".format(str(winner)))
        else:
            print("It was a sad TIE")
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

    def exportGame(self, fileName: str):
        pass
    # Get games data
    def getGamesReport(self):
        pass
    
    # Private functions ?
    def __getComputerMove(self):
        retTuple = (-1,-1)
        if (1 == self.difficulty):
            while((-1,-1) == retTuple):
                tmpTuple = self.__randCompMove()
                if (enMarker.EMPTY == self.board[ tmpTuple[0] ][ tmpTuple[1] ]):
                    retTuple = tmpTuple
        # Used for the levels of difficulty
        # elif (2 == self.difficulty):
        #     pass
        # else:
        #     pass
        return retTuple
    def __getUserMove(self, enUser):
        retTuple = (-1,-1)
        boValidInput = False
        while (False == boValidInput):
            self.display()
            mark = enMarker.O if (enUser.PLAYER_ONE == enUser) else enMarker.X
            print('\n{}. Where should I put the {} mark?'.format( enUser, str(mark) ))
            userIn = input("Input the coordinates 'y x', eg. '1 2' or '2 2: ")
            boValidInput = self.__boValidateCoordinates(userIn)

            if (True == boValidInput):
                tmpTuple = tuple(int(x) for x in userIn.split(' '))
                if (enMarker.EMPTY == self.board[ tmpTuple[0] ][ tmpTuple[1] ]):
                    retTuple = tmpTuple
                else:
                    boValidInput = False
                    print("Invalid input. Already occupied")
            else:
                print('\n\n REALLY? \n\n')
        return retTuple

    def __boValidateCoordinates(self, userInput):
        boReturn = True
        splitList = userInput.split(' ')
        if (2 == len(splitList)):
            for element in splitList:
                if (False == element.isdigit()):
                    boReturn = False
                else:
                    if((2 < int(element)) or
                       (0 > int(element))):
                        boReturn = False
        else:
            boReturn = False
        return boReturn

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

        return boReturn


    # Dificulty computer movements section
    def __randCompMove(self):
        randY = randrange(0,3,1)
        randX = randrange(0,3,1)
        return (randY, randX)

if __name__ == '__main__':
    print('Wellcome to the TicTacToe game')
    rand = randrange(0,2,1)
    game = TicTacToe((enUser.COMPUTER))
    game.newGame()
    game.play()
