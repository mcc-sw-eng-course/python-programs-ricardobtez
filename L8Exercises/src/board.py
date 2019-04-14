
from enum import Enum, auto, IntEnum
from copy import deepcopy

class enBoardType(Enum):
    TIC_TAC_TOE = auto()
    INVALID_VALUE = auto()

class Board:
    def __init__(self, size: int=0, domain: list=[' ']):
        self.size = size
        self.domain = deepcopy(domain)
        self.board = [[self.domain[0] for x in range(self.size)] for y in range(self.size)]
        self.ready = True if (size > 0 and len(domain) > 1) else False
        self.type = enBoardType.INVALID_VALUE

    def setBoardInfo(self,
                     size: int,
                     domain: list,
                     boardType: enBoardType):
        if (size > 0):
            self.size = size
        else:
            raise ValueError("Invalid input for the board size")
        self.domain = deepcopy(domain)
        self.type = boardType
        self.resetBoard()

    def resetBoard(self):
        if (True == self.ready):
            self.board = [[self.domain[0] for x in range(self.size)] for y in range(self.size)]

    def getSize(self):
        return self.size
    def getDomain(self):
        return self.domain
    def getType(self):
        return self.type
    def boFillPosition(self, data, x:int, y:int):
        boReturn = False
        if ((data is in self.domain) and (self.domain[0] != data)):
            if (self.domain[0] == self.board[y][x]):
                self.board[]
        return boReturn

    def boValidateCoordinates(self, playerInput):
        boReturn = False

        if (enBoardType.TIC_TAC_TOE == self.boardType):
            boReturn = True
            splitList = playerInput.split(' ')
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

            if (True == boReturn):
                position = [int(x) for x in splitList]
                if (self.board[position[0]][position[1]] != self.domain[0]):
                    boReturn = False
        return boReturn
