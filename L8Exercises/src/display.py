# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: Game master class

import socket

class Display:
    def __init__(self):
        self.comSocket = None

        if (True == boTwoPlayers):
            self.turn = enUser.PLAYER_ONE
            self.comSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.comSocket.bind((socket.gethostname(), 8787))
            # self.comSocket.listen(5)

    def display(self, board: Board, boLocal: bool=True):
        if (True == boLocal):
            if (enBoardType.TIC_TAC_TOE == board.getType()):
                for row in range(len(board)):
                    rowStr = ''
                    if (row > 0):
                        self.__sendDataToBuffer(5*'-')
                    for column in range(len(board[row])):
                        if(column > 0):
                            rowStr += '|'
                        rowStr += str(board[row][column])
                    self.__sendDataToBuffer(rowStr)
            else:
                raise Exception("Invlaid board type")
    def displayInfo(self, data:str, boLocal:bool = True):
        if (True == boLocal):
            print(data)
        else:
            print(data)

    def receiveInfo(self, boLocal:bool = True):
        pass

    def __getUserInput(self, user: enUser):
        dataReturn = ""
        if((True == self.boTwoPlayers) and (enUser.PLAYER_ONE == user)):
            dataReturn = "0 0"
        else:
            dataReturn = input("Input the coordinates 'y x', eg. '1 2' or '2 2': ")
        return dataReturn

    def __sendDataToBuffer(self, data):
        if (True == self.boTwoPlayers):
            # self.comSocket.send
            print(data)
        else:
            print(data)