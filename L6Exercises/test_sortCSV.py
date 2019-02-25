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

NEW_FOLDER_PATH = 'tmoFolder'

class test_sortCSV(unittest.TestCase):
    def test_classCreation(self):
        tmpClass = sortCSV()
        self.assertIsNotNone(tmpClass)
    def test_validInputFileSetInputData(self):
        tmpClass = sortCSV()
        inputFileHdlr = open(VALID_INPUT_FILENAME,'w')
        inputFileHdlr.write('1,2,3,4')
        inputFileHdlr.close()
        self.assertEqual(sdError.E_OK, tmpClass.set_input_data(VALID_INPUT_FILENAME))
        remove(VALID_INPUT_FILENAME)
    def test_validInputFileSetInputDataOtherPath(self):
        tmpClass = sortCSV()
        if (not path.exists(NEW_FOLDER_PATH)):
            makedirs(NEW_FOLDER_PATH)
        inputFileHdlr = open(NEW_FOLDER_PATH + '\\' + VALID_INPUT_FILENAME,'w')
        inputFileHdlr.write('1,2,3,4')
        inputFileHdlr.close()
        self.assertEqual(sdError.E_OK, tmpClass.set_input_data(VALID_INPUT_FILENAME))
        remove(NEW_FOLDER_PATH +'\\'+VALID_INPUT_FILENAME)
        rmdir(NEW_FOLDER_PATH)


if __name__ == '__main__':
    unittest.main()