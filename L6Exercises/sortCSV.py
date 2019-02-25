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
    E_NOT_WRITE_PERMISSION = auto()
    E_NOT_READ_PERMISSION = auto()
    E_GENERIC_ERROR = auto()

    def __str__(self):
        return '{}'.format(self.name)

# Class definition
class sortCSV:
    # Default initializer
    def __init__(self):
        self.inputFile = None
        self.outpuFile = None
        self.mergeMethod = None  # To be used later

    # Set input data method definition
    def set_input_data(self, file_path_name):
        returnValue = sdError.E_GENERIC_ERROR
        if (isinstance(file_path_name, str)):
            try:
                fileHdlr = None
                if (path.exists(file_path_name)):
                    fileHdlr = open(file_path_name, 'r').close()
                    self.inputFile = file_path_name
                returnValue = sdError.E_OK
            except:
                print('Some exception raised')
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
