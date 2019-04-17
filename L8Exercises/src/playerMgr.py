
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
        # self.playerList = []
        # for element in plyrsList:
        #     if (enUser.COMPUTER == element):
        #         self.playerList.append(enUser.COMPUTER)
        #     elif (enUser.PLAYER_ONE == element):
        #         self.playerList.append(enUser.PLAYER_ONE)
        #     elif(enUser.PLAYER_TWO == element):
        #         self.playerList.append(enUser.PLAYER_TWO)
        self.playerList = deepcopy(plyrsList)
        startRandUser = randrange(0, len(self.playerList)-1, 1)
        self.currentPlayer = self.playerList[0]#self.playerList[startRandUser]
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
            # Setting up the data to send to Display Mgr

            if (enUser.PLAYER_ONE == self.currentPlayer):
                # self.displayMgr.get
                # move = move
                raise Exception("Not finished")
        # self.currentPlayer.getNextMove()
        return move
    def nextPlayer(self):
        pass
    def getCurrentPlayer(self):
        return self.currentPlayer
    def getMarker(self):
        return self.moves[self.currentPlayer]

    def __randCompMove(self, limit):
        randY = randrange(0,limit,1)
        randX = randrange(0,limit,1)
        return (randY, randX)

if __name__ == '__main__':
    plyr = PlayerMgr([enUser.COMPUTER, enUser.PLAYER_ONE], ['X','O'])
    print(plyr.getCurrentPlayer())
    print(plyr.getMarker())
    move = plyr.getNextMove()
