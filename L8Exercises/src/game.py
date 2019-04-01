# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: Game master class

from display import *
from board import *

'''
    IGame methods that need to be implemented by the childs
'''
class IGame:
    def __init__(self):
        self.board = Board()
        self.displayMgr = Display()
    def newGame(self):
        raise Exception("Not implemented by child class")
    def play(self):
        raise Exception("Not implemented by child class")
    def getGamesReport(self):
        raise Exception("Not implemented by child class")
    def display(self):
        self.displayMgr.display(self.board)