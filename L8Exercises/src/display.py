# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: Game master class

import socket

class Display:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method"""
        if (Display.__instance == None):
            Display()
        return Display.__instance

    def __init__(self):
        """ Virtually private constructor"""
        if (Display.__instance != None):
            raise Exception("This class is a singleton!")
        else:
            Display.__instance = self

        self.comSocket = None

        # if (True == boTwoPlayers):
        #     self.turn = enUser.PLAYER_ONE
        #     self.comSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     self.comSocket.bind((socket.gethostname(), 8787))
            # self.comSocket.listen(5)

    def display(self, data:str, boLocal: bool=True):
        if (True == boLocal):
            print(data)
        else:
            self.comSocket.send(data)
            
    def displayInfo(self, data:str, boLocal:bool = True):
        if (True == boLocal):
            print(data)
        else:
            print(data)

    def receiveInfo(self, boLocal:bool = True):
        pass

    # def __getUserInput(self, user: enUser):
    #     dataReturn = ""
    #     if((True == self.boTwoPlayers) and (enUser.PLAYER_ONE == user)):
    #         dataReturn = "0 0"
    #     else:
    #         dataReturn = input("Input the coordinates 'y x', eg. '1 2' or '2 2': ")
    #     return dataReturn

    def __sendDataToBuffer(self, data):
        if (True == self.boTwoPlayers):
            # self.comSocket.send
            print(data)
        else:
            print(data)

if __name__ == '__main__':
    d = Display.getInstance()
    print(d)
    e = Display.getInstance()
    print(d)
