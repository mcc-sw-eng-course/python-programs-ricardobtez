
from IPlayer import *
from random import randrange
from display import *

class PlayerMgr:
    def __init__(self, plyrsList:list, markers:list):
        self.playerList = []
        for element in plyrsList:
            if (enUser.COMPUTER == element):
                self.playerList.append(ComputerPlayer())
            elif (enUser.PLAYER_ONE == element):
                self.playerList.append(UserPlayer(enUser.PLAYER_ONE))
            elif(enUser.PLAYER_TWO == element):
                self.playerList.append(UserPlayer(enUser.PLAYER_TWO))
        startRandUser = randrange(0, len(self.playerList)-1, 1)
        self.currentPlayer = self.playerList[startRandUser]
        self.displayMgr = Display.getInstance()
        self.moves = {}

        if (len(plyrsList) == len(markers)):
            for i in range(len(self.playerList)):
                self.moves[self.playerList[i]] = markers[i]
        else:
            raise ValueError("Moves dont correspond to Players")
    def getNextMove(self):
        self.currentPlayer.getNextMove()
    def nextPlayer(self):
        pass
    def getCurrentPlayer(self):
        return self.currentPlayer
    def getMarker(self):
        return self.moves[self.currentPlayer]

if __name__ == '__main__':
    plyr = PlayerMgr([enUser.COMPUTER, enUser.PLAYER_ONE])
    print(plyr.getCurrentPlayer())
    print(plyr.getMarker())
