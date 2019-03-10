# Author: Ricardo Arturo Benitez Cruz
# Student-Id: A01018084

# Import statements
import sys
from os import path
from enum import Enum, auto
from time import perf_counter

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
        self.startTime = 0
        self.endTime = 0
        self.NbrRecords = 0
        self.boSorted = False

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
        self.startTime = perf_counter()
        if(None != self.inputFile and
           None != self.outputFile):
            lista = self.__getListFromInput()
            self.__recursiveMergeSort(lista)
            outputFileHdlr = open(self.outputFile, 'w')
            outputFileHdlr.write(','.join(lista))
            outputFileHdlr.close()
            self.boSorted = True
            self.endTime = perf_counter()
            self.NbrRecords = len(lista)
            errorCode = sdError.E_OK
        return errorCode

    # Perform heap sort in the input file and writing into the
    # output file described.
    # Will return a sdError value as a result of the operation.
    def execute_heap_sort(self):
        errorCode = sdError.E_NOT_FILES_DEFINED
        self.startTime = perf_counter()
        if (None != self.inputFile and
            None != self.outputFile):
            lista = self.__getListFromInput()
            self.__heapSort(lista)
            outputFileHdlr = open(self.outputFile, 'w')
            outputFileHdlr.write(','.join(lista))
            outputFileHdlr.close()
            self.boSorted = True
            self.endTime = perf_counter()
            self.NbrRecords = len(lista)
            errorCode = sdError.E_OK
        return errorCode

    # Perform quick sort in the input file and writing into the
    # output file described.
    # Will return a sdError valaue as a result of the operation.
    def execute_quick_sort(self):
        errorCode = sdError.E_NOT_FILES_DEFINED
        self.startTime = perf_counter()
        if (None != self.inputFile and
            None != self.outputFile):
            lista = self.__getListFromInput()
            self.__quickSort(lista, 0, len(lista)-1)
            outputFileHdlr = open(self.outputFile, 'w')
            outputFileHdlr.write(','.join(lista))
            outputFileHdlr.close()
            self.boSorted = True
            self.endTime = perf_counter()
            self.NbrRecords = len(lista)
            errorCode = sdError.E_OK
        return errorCode

    # This method will return the performnance data of the last
    # execution of sorting operation.
    # [# of records sorted, Time consumed, Start time, EndTime]
    def get_performance_data(self):
        returnStruct = [0,0.0,0,0]

        if (self.boSorted):
            returnStruct[0] = self.NbrRecords
            returnStruct[1] = self.endTime - self.startTime
            returnStruct[2] = self.startTime
            returnStruct[3] = self.endTime
        return returnStruct

    # Get list representation from the input file
    def __getListFromInput(self):
        inputFileHdlr = open(self.inputFile, 'r')
        dataInput = inputFileHdlr.read()
        inputFileHdlr.close()
        lista = dataInput.split(',')
        return lista

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

    # Performs the Heap sort
    def __heapSort(self, arr):
        n = len(arr) 
  
        # Build a maxheap. 
        for i in range(n, -1, -1): 
            self.__heapify(arr, n, i) 
      
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i] # swap 
            self.__heapify(arr, i, 0)

    # To heapify subtree rooted at index i. 
    # n is size of heap 
    def __heapify(self, arr, n, i): 
        largest = i # Initialize largest as root 
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 
      
        # See if left child of root exists and is 
        # greater than root 
        if l < n and arr[i] < arr[l]: 
            largest = l 
      
        # See if right child of root exists and is 
        # greater than root 
        if r < n and arr[largest] < arr[r]: 
            largest = r 
      
        # Change root, if needed 
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] # swap 
      
            # Heapify the root. 
            self.__heapify(arr, n, largest) 

    # Function to do Quick sort 
    def __quickSort(self, arr, low, high):
        if low < high: 
  
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.__partition(arr,low,high) 
      
            # Separately sort elements before 
            # partition and after partition 
            self.__quickSort(arr, low, pi-1) 
            self.__quickSort(arr, pi+1, high) 

    def __partition(self, arr, low, high):
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 
      
        for j in range(low , high): 
      
            # If current element is smaller than or 
            # equal to pivot 
            if   arr[j] <= pivot: 
              
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
      
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 