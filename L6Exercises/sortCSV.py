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
            inputFileHdlr = open(self.inputFile, 'r')
            dataInput = inputFileHdlr.read()
            inputFileHdlr.close()
            lista = dataInput.split(',')
            self.__recursiveMergeSort(lista)
            outputFileHdlr = open(self.outputFile, 'w')
            outputFileHdlr.write(','.join(lista))
            outputFileHdlr.close()
            errorCode = sdError.E_OK
        return errorCode

    # Will receive a list of X size and will return the sorted list
    # If an error occurs at any moment, will throw an exception
    def __recursiveMergeSort(self, arr):
        if len(arr) >1: 
            mid = len(arr)//2
            L = arr[:mid]  
            R = arr[mid:]
      
            self.__recursiveMergeSort(L) 
            self.__recursiveMergeSort(R)
      
            i = j = k = 0
              
            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1
              
            # Checking if any element was left 
            while i < len(L): 
                arr[k] = L[i] 
                i+=1
                k+=1
              
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1


if __name__ == '__main__':
    tmpClass = sortCSV()
    inputFileHdlr = open('test.csv', 'w')
    inputFileHdlr.write('10,9,8,7,6,5,4,3,2,1,0')
    inputFileHdlr.close()
    tmpClass.set_input_data('test.csv')
    tmpClass.set_output_data('out.csv')
    tmpClass.execute_merge_sort()
    outputFileHdlr = open('out.csv', 'r')
    outRead = outputFileHdlr.read()
    outputFileHdlr.close()
    print(outRead)
