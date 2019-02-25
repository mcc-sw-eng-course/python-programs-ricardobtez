# Author: Ricardo Arturo Benitez Cruz
# Student-Id: A01018084

# Import statements
import sys
from os import path
from enum import Enum, auto

# Enumeration used for error return
class sdError(Enum):
    E_OK = auto()
    E_NOT_VALID_FILE = auto()
    E_INVALID_DATA_IN_FILE = auto()
    E_NOT_WRITE_PERMISSION = auto()
    E_NOT_READ_PERMISSION = auto()
    E_GENERIC_ERROR = auto()

# Class definition
class sortCSV:
    # Default initializer
    def __init__(self):
        self.inputFile = None
        self.outpuFile = None
        self.mergeMethod = None  # To be used later

    # Set input data method definition
    def set_input_data(self, file_path_name):
        returnValue = sdError.E_OK
        if (isinstance(file_path_name, str)):
            fileHdlr = None
            if (path.exists(file_path_name)):
                try:
                    fileHdlr = open(file_path_name, 'r').close()
                except:
                    returnValue = sdError.E_NOT_READ_PERMISSION

                if (sdError.E_OK == returnValue):
                    pointsCount = file_path_name.count('.')
                    # Checking filename format
                    if (1 < pointsCount):
                        returnValue = sdError.E_NOT_VALID_FILE
                    if (file_path_name[-4:] != '.csv'):
                        returnValue = sdError.E_NOT_VALID_FILE
                    self.inputFile = file_path_name
            else:
                returnValue = sdError.E_NOT_VALID_FILE              
        else:
            raise ValueError('No valid input file_path_name')
        return returnValue

    # Set output data method definition
    def set_output_data(self, file_path_name):
        pass

    # Perform merge sort in the input file and writing into the
    # output file described
    def execute_merge_sort(self):
        pass
