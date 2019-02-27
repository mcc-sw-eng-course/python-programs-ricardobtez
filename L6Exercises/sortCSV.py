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
    E_NOT_FILES_DEFINED = auto()
    E_INVALID_DATA_IN_FILE = auto()
    E_NOT_WRITE_PERMISSION = auto()
    E_NOT_READ_PERMISSION = auto()
    E_GENERIC_ERROR = auto()

# Class definition
class sortCSV:
    # Default initializer
    def __init__(self):
        self.inputFile = None
        self.outputFile = None
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

                if (sdError.E_OK == returnValue):
                    self.inputFile = file_path_name
            else:
                returnValue = sdError.E_NOT_VALID_FILE              
        else:
            raise ValueError('No valid input file_path_name')
        return returnValue

    # Set output data method definition
    def set_output_data(self, file_path_name):
        returnValue = sdError.E_OK

        if (isinstance(file_path_name, str)):
            fileHdlr = None
            try:
                fileHdlr = open(file_path_name, 'w').close()
            except:
                returnValue = sdError.E_NOT_WRITE_PERMISSION

            if (sdError.E_OK == returnValue):
                pointsCount = file_path_name.count('.')
                # Checking filename format
                if (1 < pointsCount):
                    returnValue = sdError.E_NOT_VALID_FILE
                if (file_path_name[-4:] != '.csv'):
                    returnValue = sdError.E_NOT_VALID_FILE

            if (sdError.E_OK == returnValue):
                self.outputFile = file_path_name
        else:
            raise ValueError('No valid output file_path_name')
        return returnValue

    # Perform merge sort in the input file and writing into the
    # output file described
    # Will return a sdError value as a result of the operation
    def execute_merge_sort(self):
        errorCode = sdError.E_NOT_FILES_DEFINED
        finelResult = []
        if(None != self.inputFile and
           None != self.outputFile):
            dataInput = open(self.inputFile, 'r').read().close()
            finalResult = self.__recursiveMergeSort(dataInput.split(','))
            errorCode = sdError.E_OK
        return errorCode

    # Will receive a list of X size and will return the sorted list
    # If an error occurs at any moment, will throw an exception
    def __recursiveMergeSort(self, array):
        if(len(array) > 0):
            mid = len(array) // 2
            leftArray = array[:mid]
            rightArray = array[mid:]

            self.__recursiveMergeSort(leftArray)
            self.__recursiveMergeSort(rightArray)

            i = 0
            j = 0
            k = 0
            # Copy data to temp arrays leftArray and rightArray
            while (i < len(leftArray) and j < len(rightArray)):
                if (leftArray[i] < rightArray[i]):
                    array[k] = leftArray[i]
                    i += 1
                else:
                    array[k] = rightArray[j]
                    j += 1
                k += 1
            # Checking that all the elements are ncluded
            while (i < len(leftArray)):
                array[k] = leftArray[i]
                i += 1
                k += 1
            while(j < len(rightArray)):
                array[k] = rightArray[j]
                j += 1
                k += 1



