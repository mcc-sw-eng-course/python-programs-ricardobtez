# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: Player Manager class

from enum import auto, IntEnum
from random import randrange
from display import *
from board import Board
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

        if (len(plyrsList) == len(markers)):
            for i in range(len(self.playerList)):
                self.moves[self.playerList[i]] = markers[i]
        else:
            raise ValueError("Moves dont correspond to Players")
    def getNextMove(self, board:Board):
        move = (-1,-1)
        if (enUser.COMPUTER == self.currentPlayer):
            move = self.__randCompMove(board.getSize())
        else:
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
        
