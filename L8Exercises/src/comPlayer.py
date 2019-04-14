
from random import randrange

class ComputerPlayer(IPlayer):
    def __init__(self):
        super(ComputerPlayer, self).__init__(enUser.COMPUTER)

    def getNextMove(self, board: Board):
        retTuple = (-1,-1)
        while((-1,-1) == retTuple):
            tmpTuple = self.__randCompMove(board)
            if (" " == board[ tmpTuple[0] ][ tmpTuple[1] ]):
                retTuple = tmpTuple
        return retTuple

    def __randCompMove(self, board: Board):
        size = board.getBoardSize()
        randY = randrange(0,size,1)
        randX = randrange(0,size,1)
        return (randY, randX)