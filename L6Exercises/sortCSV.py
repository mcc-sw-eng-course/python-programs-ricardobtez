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
            finalResult = self.__iterativeMergeSort(dataInput.split(','))
            errorCode = sdError.E_OK
        return errorCode

    # Will receive a list of X size and will return the sorted list
    # If an error occurs at any moment, will throw an exception
    def __iterativeMergeSort(self, array):
        if(len(array) > 0):
            current_size = 1
      
        # Outer loop for traversing Each  
        # sub array of current_size 
        while current_size < len(array) - 1: 
              
            left = 0
            # Inner loop for merge call  
            # in a sub array 
            # Each complete Iteration sorts 
            # the iterating sub array 
            while left < len(array)-1: 
                  
                # mid index = left index of  
                # sub array + current sub  
                # array size - 1 
                mid = left + current_size - 1
                  
                # (False result,True result) 
                # [Condition] Can use current_size 
                # if 2 * current_size < len(a)-1 
                # else len(a)-1 
                right = ((2 * current_size + left - 1, len(array) - 1)
                    [2 * current_size  + left - 1 > len(array)-1]) 
                                
                # Merge call for each sub array 
                self.__merge(array, left, mid, right) 
                left = left + current_size*2
                  
            # Increasing sub array size by 
            # multiple of 2 
            current_size = 2 * current_size
    def __merge(self, array, left, mid, right):
        print('Array:{}, left:{}, mid:{}, right{}'.format(array, left, mid, right))
        n1 = mid - left +1
        n2 = right - mid 
        L = [0] * n1
        R = [0] * n2 
        for i in range(0, n1): 
            L[i] = array[left + i] 
        for i in range(0, n2): 
            R[i] = array[mid + i + 1] 
      
        i = 0
        j = 0
        k = left 
        while i < n1 and j < n2: 
            if L[i] > R[j]: 
                array[k] = R[j] 
                j += 1
            else: 
                array[k] = L[i] 
                i += 1
            k += 1
      
        while i < n1: 
            array[k] = L[i] 
            i += 1
            k += 1
      
        while j < n2: 
            array[k] = R[j] 
            j += 1
            k += 1



