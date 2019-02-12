# Authors: Ricardo Benitez  A01018084,
#          Samuel Solorzano Axxxxxxxx

import unittest
from pastExercises import *

class test_userMathFunctions(unittest.TestCase):
    def setup(self):
        pass
    def terDown(self):
        pass
    def test_meanOnlyNumbers(self):
        lista = [1,2,3,4,5,6,7]
        self.assertEqual(mean(lista), 4)
    def test_meanNumbersAndStrings(self):
        lista = [1,2,3,'a',5,6,7]
        self.assertRaises(ValueError, mean, lista)


class tets_myPowerListFunctions(unittest.TestCase):
    def setup(self):
        pass
    def tearDow(self):
        pass

class tets_userDataClass(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
