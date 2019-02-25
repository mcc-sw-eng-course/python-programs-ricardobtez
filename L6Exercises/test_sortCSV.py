# Author: Ricardo Arturo Benitez Cruz
# Student-Id: A01018084

import unittest
from os import path, makedirs, remove, rmdir
from sortCSV import *

VALID_INPUT_FILENAME = 'inputFile.csv'
INVALID_INPUT_FILENAME = 'invalidInputFile.csv'
INVALID_INPUT_NAME_FILENAME = 'invalidInFilaname.csv.tmp'

VALID_OUTPUT_FILENAME = 'outputFile.csv'
INVALID_OUTPUT_FILENAME = 'invalidOutputFile.csv'
INVALID_OUTPUT_NAME_FILENAME = 'invalidOutFilaname.csv.tmp'

NEW_FOLDER_PATH = 'tmpFolder'

class test_sortCSV(unittest.TestCase):
    def test_classCreation(self):
        tmpClass = sortCSV()
        self.assertIsNotNone(tmpClass)

    # Positive testing set input data function
    def test_validInputFile_SetInputData(self):
        tmpClass = sortCSV()
        inputFileHdlr = open(VALID_INPUT_FILENAME,'w')
        inputFileHdlr.write('1,2,3,4')
        inputFileHdlr.close()
        self.assertEqual(sdError.E_OK, tmpClass.set_input_data(VALID_INPUT_FILENAME))
        remove(VALID_INPUT_FILENAME)
    def test_validInputFile_SetInputData_OtherPath(self):
        tmpClass = sortCSV()
        if (not path.exists(NEW_FOLDER_PATH)):
            makedirs(NEW_FOLDER_PATH)
        inputFileHdlr = open(NEW_FOLDER_PATH + '/' + VALID_INPUT_FILENAME,'w')
        inputFileHdlr.write('1,2,3,4')
        inputFileHdlr.close()
        self.assertEqual(sdError.E_OK, tmpClass.set_input_data(NEW_FOLDER_PATH + '/' + VALID_INPUT_FILENAME))
        remove(NEW_FOLDER_PATH +'/'+VALID_INPUT_FILENAME)
        rmdir(NEW_FOLDER_PATH)

    # Negative testing input file
    # def test_invalidInputFile_SetInputData(self):
    #     tmpClass = sortCSV()
    #     inputFileHdlr = open(INVALID_INPUT_FILENAME,'w')
    #     inputFileHdlr.write('1,2,3,a,b,c')
    #     inputFileHdlr.close()
    #     self.assertEqual(sdError.E_INVALID_DATA_IN_FILE, tmpClass.set_input_data(INVALID_INPUT_FILENAME))
    #     remove(INVALID_INPUT_FILENAME)
    def test_invalidFileName_SetInputData(self):
        tmpClass = sortCSV()
        inputFileHdlr = open(INVALID_INPUT_NAME_FILENAME, 'w')
        inputFileHdlr.write('1,2,3,4')
        inputFileHdlr.close()
        self.assertEqual(sdError.E_NOT_VALID_FILE, tmpClass.set_input_data(INVALID_INPUT_NAME_FILENAME))
        remove(INVALID_INPUT_NAME_FILENAME)
    def test_fileNotExistent_SetInputData(self):
        tmpClass = sortCSV()
        self.assertEqual(sdError.E_NOT_VALID_FILE, tmpClass.set_input_data('some'+VALID_INPUT_FILENAME))
    def test_tuppleInsteadOfStr_SetInputData(self):
        tmpClass = sortCSV()
        self.assertRaises(ValueError, tmpClass.set_input_data, [VALID_INPUT_FILENAME])



if __name__ == '__main__':
    unittest.main()