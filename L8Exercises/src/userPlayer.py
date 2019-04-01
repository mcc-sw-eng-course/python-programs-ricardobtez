
from IPlayer import *
from display import *

class UserPlayer(IPlayer):
    def __init__(self, playerId):
        super(UserPlayer, self).__init__(playerId)

    def getNextMove(self, board: Board):
        retTuple = (-1,-1)
        boValidInput = False
        while (False == boValidInput):
            mark = enMarker.O if (enUser.PLAYER_ONE == self.playerId) else enMarker.X
            self.displayMgr.displayInfo('\n{}. Where should I put the {} mark?'.format( self.playerId, str(mark) ))
            userIn = self.displayMgr.receiveInfo(self.playerId)
            boValidInput = board.boValidateCoordinates(userIn)

            if (True == boValidInput):
                tmpTuple = tuple(int(x) for x in userIn.split(' '))
                if (enMarker.EMPTY == self.board[ tmpTuple[0] ][ tmpTuple[1] ]):
                    retTuple = tmpTuple
                else:
                    boValidInput = False
                    self.displayMgr.displayInfo("Invalid input. Already occupied")
            else:
                self.displayMgr.displayInfo('\n\n REALLY? \n\n')
        return retTuple