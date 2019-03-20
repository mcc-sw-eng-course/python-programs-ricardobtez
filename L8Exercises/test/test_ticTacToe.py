# Author: Ricardo Arturo Benitez Cruz
# Student number: A01018084
# Program: Test for the TicTacToe

import sys
sys.path.append('./aux')
sys.path.append('../src')
import unittest
from tic_tac_toe import TicTacToe, enMarker
from copy import deepcopy
from os import remove

TMP_FILENAME = 'aux/tmp_file.txt'
AUX_FILENAME = 'aux/aux_testFile1.txt'
AUX_FILENAME2 = 'aux/aux_testFile2.txt'
AUX_FILENAME3 = 'aux/aux_testFile3.txt'
AUX_FILENAME4 = 'aux/aux_testFile4.txt'
AUX_FILENAME5 = 'aux/aux_testFile5.txt'

# Auxiliary funciton used to find the markers in the
# tictactoe board. Returns a list of tupples with the coordinates.
# For error handling it will return an empty list
def searchMarkers(board, marker):
    xReturnList = []
    errorFound = False
    if ((enMarker.X == marker or enMarker.O == marker) and
        (isinstance(board, list))):
        for row in range(len(board)):
            for column in range(len(board[row])):
                if (marker == board[row][column]):
                    xReturnList.append((row,column))
                if (False == isinstance(board[row][column], enMarker)):
                    errorFound = True
                    break
            if (True == errorFound):
                xReturnList = []
                break
    return xReturnList

def createBoardFromFile(fileName):
    # Creates empty board to be later filled
    board = [[enMarker.EMPTY for x in range(3)] for y in range(3)]
    fileHdlr = open(fileName, 'r')
    yIndex = 0
    for line in fileHdlr:
        if(line[0] != '-'):
            lineList = line.strip().split('|')
            for xIndex in range(len(lineList)):
                if ('X' == lineList[xIndex]):
                    board[yIndex][xIndex] = enMarker.X
                elif('O' == lineList[xIndex]):
                    board[yIndex][xIndex] = enMarker.O
            yIndex += 1
    fileHdlr.close()
    return board

# Auxiliary test class
class test_auxiliaryFunctions(unittest.TestCase):
    def setUp(self):
        self.test_board = [[enMarker.EMPTY for x in range(3)] for y in range(3)]
        self.test_invalidBoard_numbers = [x for x in range(10)]
        self.test_invalidBoard_string = [str(x) for x in range(10)]
        self.test_invalidBoard_InvalidChar = [[enMarker.EMPTY for x in range(3)] for y in range(3)]
        self.test_invalidBoard_InvalidChar[1][1] = 'InvalidData'

    def test_positive_circleMarkerIn_0_0(self):
        tmpBoard = deepcopy(self.test_board)
        tmpBoard[0][0] = enMarker.O
        self.assertEqual( [(0,0)], searchMarkers(tmpBoard, enMarker.O))
    def test_positive_circleMarkerIn_0_0_and_1_1(self):
        tmpBoard = deepcopy(self.test_board)
        tmpBoard[0][0] = enMarker.O
        tmpBoard[1][1] = enMarker.O
        self.assertEqual( [(0,0),(1,1)], searchMarkers(tmpBoard, enMarker.O))
    def test_positive_crossMarkerIn_1_1(self):
        tmpBoard = deepcopy(self.test_board)
        tmpBoard[1][1] = enMarker.X
        self.assertEqual( [(1,1)], searchMarkers(tmpBoard, enMarker.X))
    def test_positive_crossMarkerIn_1_1_and_2_2(self):
        tmpBoard = deepcopy(self.test_board)
        tmpBoard[1][1] = enMarker.X
        tmpBoard[2][2] = enMarker.X
        self.assertEqual( [(1,1), (2,2)], searchMarkers(tmpBoard, enMarker.X))
    def test_positive_noMarkersInBoard_circle(self):
        self.assertEqual( [], searchMarkers(self.test_board, enMarker.O))
    def test_positive_noMarkersInBoard_cross(self):
        self.assertEqual( [], searchMarkers(self.test_board, enMarker.X))

    def test_positive_getBoardValidFile(self):
        board = [[enMarker.EMPTY for x in range(3)] for y in range(3)]
        board[0][0] = enMarker.X
        boardFile = createBoardFromFile(AUX_FILENAME)
        self.assertEqual(board, boardFile)
    # Negative Testing
    def test_negative_InvalidBoard_listOfNumbers_circle(self):
        self.assertRaises( TypeError, searchMarkers, self.test_invalidBoard_numbers, enMarker.O)
    def test_negative_InvalidBoard_listOfNumbers_cross(self):
        self.assertRaises( TypeError, searchMarkers, self.test_invalidBoard_numbers, enMarker.X)
    def test_negative_InvalidBoard_listOfStr_circle(self):
        self.assertEqual( [], searchMarkers(self.test_invalidBoard_string, enMarker.O))
    def test_negative_InvalidBoard_listOfStr_cross(self):
        self.assertEqual( [], searchMarkers(self.test_invalidBoard_string, enMarker.X))

# Main test class
class test_ticTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe(0)
    def tearDown(self):
        pass
    def test_positive_gameCreation(self):
        self.assertIsNotNone(self.game)
    def test_positive_newGameValid(self):
        # Makes sure the game has a fresh start
        self.game.newGame()
        fileHdlr = open(TMP_FILENAME, 'w')
        # redirects the stdout to the file specified to be read later
        sys.stdout = fileHdlr
        self.game.display()
        sys.stdout = sys.__stdout__
        fileHdlr.close()
        board = createBoardFromFile(TMP_FILENAME)
        self.assertEqual(0, len(searchMarkers(board, enMarker.X)))
        remove(TMP_FILENAME)
    def test_positive_computerMoveValid(self):
        # game = TicTacToe()
        self.game.newGame()
        compTuple = self.game._TicTacToe__getComputerMove()
        self.assertNotEqual((-1,-1), compTuple)
    # Too complicated at the moment
    # Wil need to modify stdin and stdout to test this functionality
    # def test_positive_userMoveValid(self):
    #     self.game.newGame()
    #     compTuple = self.game._TicTacToe__getUserMove()
    #     self.assertEqual((2,2), compTuple)

    # Test cases for the play will also be delayed because of the complexity

    def test_positive_importGame_simpleGame(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME)
        fileHdlr = open(TMP_FILENAME, 'w')
        sys.stdout = fileHdlr
        self.game.display()
        sys.stdout = sys.__stdout__
        fileHdlr.close()
        board = createBoardFromFile(TMP_FILENAME)
        self.assertEqual(1, len(searchMarkers(board, enMarker.X)))
        remove(TMP_FILENAME)
    def test_positive_importGame_complicatedGame(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME2)
        fileHdlr = open(TMP_FILENAME, 'w')
        sys.stdout = fileHdlr
        self.game.display()
        sys.stdout = sys.__stdout__
        fileHdlr.close()
        board = createBoardFromFile(TMP_FILENAME)
        self.assertEqual(4, len(searchMarkers(board, enMarker.X)))
        remove(TMP_FILENAME)


    def test_positive_validateCoordinates_0_0(self):
        self.assertTrue(self.game._TicTacToe__boValidateCoordinates('0 0'))
    def test_positive_validateCoordinates_0_1(self):
        self.assertTrue(self.game._TicTacToe__boValidateCoordinates('0 1'))
    def test_positive_validateCoordinates_2_0(self):
        self.assertTrue(self.game._TicTacToe__boValidateCoordinates('2 0'))
    def test_positive_validateCoordinates_2_2(self):
        self.assertTrue(self.game._TicTacToe__boValidateCoordinates('2 2'))
    def test_positive_validateCoordinates_1_1(self):
        self.assertTrue(self.game._TicTacToe__boValidateCoordinates('0 0'))

    def test_positive_randomComputerMove(self):
        self.assertNotEqual((-1,-1), self.game._TicTacToe__randCompMove())

    def test_positive_boCheckHorRow_0(self):
        self.game.newGame()
        self.assertFalse(self.game._TicTacToe__boCheckHorRow(0))
    def test_positive_boCheckHorRow_1(self):
        self.game.newGame()
        self.assertFalse(self.game._TicTacToe__boCheckHorRow(1))
    def test_positive_boCheckHorRow_2(self):
        self.game.newGame()
        self.assertFalse(self.game._TicTacToe__boCheckHorRow(2))
    def test_positive_boCheckHorRow_AlmostFinishedGame_0(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME3)
        self.assertTrue(self.game._TicTacToe__boCheckHorRow(0))
    def test_positive_boCheckHorRow_AlmostFinishedGame_1(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME3)
        self.assertTrue(self.game._TicTacToe__boCheckHorRow(1))
    def test_positive_boCheckHorRow_AlmostFinishedGame_2(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME3)
        self.assertFalse(self.game._TicTacToe__boCheckHorRow(2))

    def test_positive_boCheckVerCol_0(self):
        self.game.newGame()
        self.assertFalse(self.game._TicTacToe__boCheckVerCol(0))
    def test_positive_boCheckVerCol_1(self):
        self.game.newGame()
        self.assertFalse(self.game._TicTacToe__boCheckVerCol(1))
    def test_positive_boCheckVerCol_2(self):
        self.game.newGame()
        self.assertFalse(self.game._TicTacToe__boCheckVerCol(2))
    def test_positive_boCheckVerCol_AlmostFinishedGame_0(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME4)
        self.assertTrue(self.game._TicTacToe__boCheckVerCol(0))
    def test_positive_boCheckVerCol_AlmostFinishedGame_1(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME4)
        self.assertTrue(self.game._TicTacToe__boCheckVerCol(1))
    def test_positive_boCheckVerCol_AlmostFinishedGame_2(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME4)
        self.assertFalse(self.game._TicTacToe__boCheckVerCol(2))

    def test_positive_boCheckDiagRow_AlmostFinishedGame_File2_True(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME2)
        self.assertFalse(self.game._TicTacToe__boCheckDiag(True))
    def test_positive_boCheckDiagRow_AlmostFinishedGame_File3_True(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME3)
        self.assertFalse(self.game._TicTacToe__boCheckDiag(True))
    def test_positive_boCheckDiagRow_AlmostFinishedGame_File4_True(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME4)
        self.assertFalse(self.game._TicTacToe__boCheckDiag(True))
    def test_positive_boCheckDiagRow_AlmostFinishedGame_File5_True(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME5)
        self.assertTrue(self.game._TicTacToe__boCheckDiag(True))
    def test_positive_boCheckDiagRow_AlmostFinishedGame_File2_False(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME2)
        self.assertTrue(self.game._TicTacToe__boCheckDiag(False))
    def test_positive_boCheckDiagRow_AlmostFinishedGame_File3_False(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME3)
        self.assertFalse(self.game._TicTacToe__boCheckDiag(False))
    def test_positive_boCheckDiagRow_AlmostFinishedGame_File4_False(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME4)
        self.assertFalse(self.game._TicTacToe__boCheckDiag(False))
    def test_positive_boCheckDiagRow_AlmostFinishedGame_File5_False(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME5)
        self.assertTrue(self.game._TicTacToe__boCheckDiag(False))

    def test_positive_boGameWon_AlmostFinishedGame_File3_0_0(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME3)
        self.assertTrue(self.game._TicTacToe__boPlayerWon(0,0))
    def test_positive_boGameWon_AlmostFinishedGame_File3_0_1(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME3)
        self.assertTrue(self.game._TicTacToe__boPlayerWon(0,1))
    def test_positive_boGameWon_AlmostFinishedGame_File3_2_1(self):
        self.game.newGame()
        self.game.importGame(AUX_FILENAME3)
        # self.game.display()
        self.assertFalse(self.game._TicTacToe__boPlayerWon(2,1))

    # Negative testing
    def test_negative_validateCoordinates_2_3(self):
        self.assertFalse(self.game._TicTacToe__boValidateCoordinates('2 3'))
    def test_negative_validateCoordinates_4_0(self):
        self.assertFalse(self.game._TicTacToe__boValidateCoordinates('4 0'))
    def test_negative_validateCoordinates_0_0_0(self):
        self.assertFalse(self.game._TicTacToe__boValidateCoordinates('0 0 0'))
    def test_negative_validateCoordinates_2Dot5_0(self):
        self.assertFalse(self.game._TicTacToe__boValidateCoordinates('2.5 0'))
    def test_negative_validateCoordinates_Minus1_0(self):
        self.assertFalse(self.game._TicTacToe__boValidateCoordinates('-1 0'))

    def test_negative_boCheckHorRow_3(self):
        self.game.newGame()
        self.assertRaises(ValueError, self.game._TicTacToe__boCheckHorRow, 3)
    def test_negative_boCheckHorRow_Minus1(self):
        self.game.newGame()
        self.assertRaises(ValueError, self.game._TicTacToe__boCheckHorRow, -1)

    def test_negative_boCheckVerCol_3(self):
        self.game.newGame()
        self.assertRaises(ValueError, self.game._TicTacToe__boCheckVerCol, 3)
    def test_negative_boCheckVerCol_Minus1(self):
        self.game.newGame()
        self.assertRaises(ValueError, self.game._TicTacToe__boCheckVerCol, -1)

if __name__ == '__main__':
    unittest.main()