
from enum import Enum, auto, IntEnum
from board import Board

class enUser(Enum):
    COMPUTER = auto()
    PLAYER_ONE = auto()
    PLAYER_TWO = auto()
    INVALID_USER = auto()

    def __str__(self):
        return str(self.name)

class IPlayer:
    def __init__(self, playerId: enUser):
        if (playerId < enUser.INVALID_USER):
            self.playerId = playerId
        else:
            self.playerId = enUser.INVALID_USER
        self.displayMgr = Display()
    def getPlayerId(self):
        return self.playerId

    def getNextMove(self, board: Board):
        raise Exception("Not implemented by child class")