# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: Player Manager class

from enum import auto, IntEnum
from random import randrange
from display import *
from board import Board, enBoardType
from copy import deepcopy

class enUser(IntEnum):
    COMPUTER = auto()
    PLAYER_ONE = auto()
    PLAYER_TWO = auto()
    INVALID_USER = auto()

    def __str__(self):
        return str(self.name)

class PlayerMgr:
    def __init__(self, plyrsList:list, markers:list):
        self.playerList = deepcopy(plyrsList)
        startRandUser = randrange(0, len(self.playerList), 1)
        self.currentPlayer = self.playerList[startRandUser]
        self.currenIndexPlayer = startRandUser
        self.displayMgr = Display.getInstance()
        self.moves = {}

        # if (len(plyrsList) == len(markers)):
        for i in range(len(self.playerList)):
            self.moves[self.playerList[i]] = markers[i]
        # else:
        #     raise ValueError("Moves dont correspond to Players")
    def getNextMove(self, board:Board):
        move = (-1,-1)
        if (enUser.COMPUTER == self.currentPlayer):
            if (board.getType() == enBoardType.TIC_TAC_TOE):
                move = self.__randCompMove(board.getSize())
            else:
                move = self.__randCheckersMove(board)
        else:
            if (board.getType() == enBoardType.TIC_TAC_TOE):
                if (enUser.PLAYER_ONE == self.currentPlayer):
                    while(move == (-1, -1)):
                        self.displayMgr.display(str(board))
                        data = self.displayMgr.receiveInfo("Input the coordinates 'y x', eg. '0 2' or '2 2': ")
                        dataList = data.split(" ")
                        if (2==len(dataList)):
                            if((dataList[0].isdigit()) and (dataList[1].isdigit())):
                                move = (int(dataList[0]), int(dataList[1]))
                            else:
                                self.displayMgr.display("REALLY?! Try again")
                        else:
                            self.displayMgr.display("Wrong input.")
                if (enUser.PLAYER_TWO == self.currentPlayer):
                    raise Exception("Not finished")
            else:
                pass
        return move
    def nextPlayer(self):
        self.currenIndexPlayer = ((self.currenIndexPlayer + 1) % len(self.playerList))
        self.currentPlayer = self.playerList[self.currenIndexPlayer]
    def getCurrentPlayer(self):
        return self.currentPlayer
    def getMarker(self):
        return self.moves[self.currentPlayer]

    def __randCompMove(self, limit):
        randY = randrange(0,limit,1)
        randX = randrange(0,limit,1)
        return (randY, randX)
    def __randCheckersMove(self, board: Board):
        xReturn = None
        whitesPosition = self.__getPlayersPieces(board, enUser.COMPUTER)
        redsPosition = self.__getPlayersPieces(board, enUser.PLAYER_ONE)
        moves = self.__sortPlayersPieces(whitesPosition, redsPosition)
        return xReturn

    def __getPlayersPieces(self, board:Board, user:enUser):
        aReturn = []
        # Gets all the positions of the current Computer coins
        for row in range(8):
            for column in range(8):
                cellData = board.getDomainInCell(row, column)
                if (cellData == self.moves[user]):
                    aReturn.append([row,column])
        return aReturn

    def __sortPlayersPieces(self,
                            ownPlayerPositions: list,
                            versusPLayerPositions: list,
                            boDirection: bool=True):
        sortedList = []
        for position in ownPlayerPositions:
            pass

    def __getAllMovesPosition(self, board: Board, position):
        value = board.getDomainInCell(position[0], position[1])
        xAllMoves = []
        if (enChecker.RED == value):

            if (enChecker.EMPTY == board.getDomainInCell((position[0]-1) % 8,
                                                         (position[1]-1) % 8)):
                xAllMoves.append([(position[0]-1) % 8,(position[1]-1) % 8])
            # if (enChecker.WHITE == board.getDomainInCell((position[0]-1) % 8,
            #                                              (position[1]-1) % 8)):
            #     xAllMoves.append(self.__getAllMovesPosition(board, [position[0]]))
            # if (enChecker.EMPTY == board.getDomainInCell((position[0]-1) % 8,
            #                                              (position[1]+1) % 8)):
        # if ((value == enChecker.RED_KING) or (value == enChecker.WHITE_KING)):

        return xAllMoves
