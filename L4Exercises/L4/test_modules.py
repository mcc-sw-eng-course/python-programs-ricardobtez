import sys
sys.path.append('../L1.8')
sys.path.append('../L1.9')
sys.path.append('../L2.10-14')
sys.path.append('../L2.15')
import unittest
from l1_8_module import *
from module import *
from myPowerList import *
from UserDirectory import *

import os

class test_l4_unittest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # get_sample_mean
    def test_mean_SameValueList(self):
        test_list = [2,2,2,2,2]
        self.assertEqual(2, get_sample_mean(test_list))

    def test_mean_OneElementList(self):
        test_list = [2]
        self.assertEqual(2, get_sample_mean(test_list))

    def test_mean_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_sample_mean(test_list))

    def test_mean_InvalidList(self):
        test_list = 789
        self.assertEqual(0, get_sample_mean(test_list))

    def test_mean_ListWithNumberStrings(self):
        test_list = ["5", "5", "5", "5", "5"]
        self.assertEqual(5, get_sample_mean(test_list))

    def test_mean_ListWithTextStrings(self):
        test_list = ["abc", "def", "ghi", "jkl", "mno"]
        self.assertRaises(ValueError, get_sample_mean, test_list)

    # get_sample_standard_dev
    def test_stdDev_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_sample_standard_dev(test_list))

    def test_stdDev_NotAlList(self):
        test_list = 200
        self.assertEqual(0, get_sample_standard_dev(test_list))

    def test_stdDev_ListWithNumberStrings(self):
        test_list = ["5", "5", "5", "5", "5"]
        self.assertEqual(0, get_sample_standard_dev(test_list))

    def test_stdDev_ListWithTextStrings(self):
        test_list = ["abc", "def", "ghi", "jkl", "mno"]
        self.assertRaises(ValueError, get_sample_standard_dev, test_list)

    def test_stdDev_ValidList(self):
        test_list = [1,2,3,4,5]
        self.assertEqual(1.4142135623730951, get_sample_standard_dev(test_list))

    # get_sample_median
    def test_median_ValidListOdd(self):
        test_list = [1,2,3,4,5]
        self.assertEqual(3, get_sample_median(test_list))

    def test_median_ValidListEven(self):
        test_list = [1,2,3,4,5,6]
        self.assertEqual(3.5, get_sample_median(test_list))

    def test_median_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_sample_median(test_list))

    def test_median_NotAList(self):
        test_list = 450
        self.assertEqual(0, get_sample_median(test_list))

    # get_n_quartil
    def test_quartil_NotAList(self):
        test_list = 450
        self.assertEqual(0, get_n_quartil(Quartil.LOW, test_list))

    def test_quartil_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_n_quartil(Quartil.LOW, test_list))

    def test_quartil_LowQuartilEven(self):
        test_list = [1,2,3,5,4,6,7,10,9,8]
        self.assertEqual(3, get_n_quartil(Quartil.LOW, test_list))

    def test_quartil_LowQuartilOdd(self):
        test_list = [1,2,3,5,4,6,7,10,9,8,11]
        self.assertEqual(3, get_n_quartil(Quartil.LOW, test_list))

    def test_quartil_MidQuartilEven(self):
        test_list = [1,2,3,5,4,6,7,10,9,8]
        self.assertEqual(5.5, get_n_quartil(Quartil.MID, test_list))

    def test_quartil_MidQuartilOdd(self):
        test_list = [1,2,3,5,4,6,7,10,9,8,11]
        self.assertEqual(6, get_n_quartil(Quartil.MID, test_list))

    def test_quartil_HighSQuartilEven(self):
        test_list = [1,2,3,5,4,6,7,10,9,8]
        self.assertEqual(8, get_n_quartil(Quartil.HIGH, test_list))

    def test_quartil_HighQuartilOdd(self):
        test_list = [1,2,3,5,4,6,7,10,9,8,11]
        self.assertEqual(9, get_n_quartil(Quartil.HIGH, test_list))

    def test_quartil_InvalidQuartil(self):
        test_list = [1,2,3,5,4,6,7,10,9,8,11]
        self.assertEqual(None, get_n_quartil(5, test_list))

    # get_n_percentil
    def test_percentil_NotAList(self):
        test_list = 50
        self.assertEqual(0, get_n_percentil(0, test_list))

    def test_percentil_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_n_percentil(0, test_list))

    def test_percentil_ValidPerc(self):
        test_list = [1,2,3,5,4,6,7,10,9,8]
        self.assertEqual(6, get_n_percentil(0.5, test_list))

    # to_roman_format
    def test_toroman_correct(self):
        self.assertEqual("M", to_roman_format(1000))

    def test_toroman_outOfRangeMin(self):
        self.assertEqual("", to_roman_format(0))

    def test_toroman_outOfRangeMax(self):
        self.assertEqual("", to_roman_format(5000))

    # myPowerList
    def test_powerlist_addItem(self):
        my_list = myPowerList()
        my_list.addItem(5)
        self.assertEqual(1, len(my_list.m_list))

    def test_powerlist_removeItem(self):
        my_list = myPowerList()
        my_list.addItem(5)
        my_list.addItem(6)
        my_list.addItem(7)
        my_list.removeItem(1)
        self.assertEqual([5,7], my_list.m_list)

    def test_powerlist_sortList(self):
        my_list = myPowerList()
        my_list.addItem(6)
        my_list.addItem(7)
        my_list.addItem(10)
        my_list.addItem(1)
        my_list.addItem(5)
        self.assertEqual([1,5,6,7,10], my_list.sortList())

    def test_powerlist_left_merge(self):
        my_list = myPowerList()
        my_list.addItem(5)
        my_list.Lmerge([1,2,3,4])
        self.assertEqual([1,2,3,4,5], my_list.m_list)

    def test_powerlist_right_merge(self):
        my_list = myPowerList()
        my_list.addItem(5)
        my_list.Rmerge([1,2,3,4])
        self.assertEqual([5,1,2,3,4], my_list.m_list)

    def test_powerlist_SaveReadToFile(self):
        my_list = myPowerList()
        my_list.addItem(5)
        my_list.addItem(10)
        my_list.addItem(15)
        my_list.addItem(20)
        my_list.saveToTextFile("MyTestList.txt")
        new_list = myPowerList()
        new_list.readFromTextFile("MyTestList.txt")
        self.assertListEqual(my_list.m_list, new_list.m_list)
        os.remove("MyTestList.txt")

    # UserDirectory
    def test_userdir_addRecord(self):
        d = UserDirectory()
        d.addRecord("Sam", "Calle Falsa", "1234567", "sam@sam.com")
        d.addRecord("Pepe", "Calle 123", "789456", "peps@pepito.com")
        self.assertEqual(2, len(d.m_directory))

    def test_userdir_save_read_file(self):
        d1 = UserDirectory()
        d1.addRecord("Sam", "Calle Falsa", "1234567", "sam@sam.com")
        d1.addRecord("Pepe", "Calle 123", "789456", "peps@pepito.com")
        d1.saveDirectoryToFile("myTestDir.txt")
        d2 = UserDirectory()
        d2.readDirectoryFromFile("myTestDir.txt")
        self.assertListEqual(d1.m_directory, d2.m_directory)
        os.remove("myTestDir.txt")

    def test_userdir_search(self):
        d = UserDirectory()
        name, address, phone, mail = "Sam", "Calle Falsa", "123456", "sam@sam.com"
        d.addRecord(name, address, phone, mail)
        name_record = { 
                UserDataType.NAME : name,
                UserDataType.ADDRESS : address,
                UserDataType.PHONE : phone,
                UserDataType.MAIL : mail,
            }
        name, address, phone, mail = "Pepe", "Calle 123", "789456", "peps@pepito.com"
        d.addRecord(name, address, phone, mail)
        address_record = { 
                UserDataType.NAME : name,
                UserDataType.ADDRESS : address,
                UserDataType.PHONE : phone,
                UserDataType.MAIL : mail,
            }
        name, address, phone, mail = "Juan", "Calle Roca", "134679", "juanito@juancho.com"
        d.addRecord(name, address, phone, mail)
        phone_record = { 
                UserDataType.NAME : name,
                UserDataType.ADDRESS : address,
                UserDataType.PHONE : phone,
                UserDataType.MAIL : mail,
            }
        name, address, phone, mail = "Perla", "Av Gral", "857496", "perla@facebook.com"
        d.addRecord(name, address, phone, mail)
        mail_record = { 
                UserDataType.NAME : name,
                UserDataType.ADDRESS : address,
                UserDataType.PHONE : phone,
                UserDataType.MAIL : mail,
            }

        # find by name
        searched_record = d.searchForRecord(UserDataType.NAME, "Sam")
        self.assertDictEqual(name_record, searched_record)

        # find by address
        searched_record = d.searchForRecord(UserDataType.ADDRESS, "Calle 123")
        self.assertDictEqual(address_record, searched_record)

        # find by name
        searched_record = d.searchForRecord(UserDataType.PHONE, "134679")
        self.assertDictEqual(phone_record, searched_record)

        # find by name
        searched_record = d.searchForRecord(UserDataType.MAIL, "perla@facebook.com")
        self.assertDictEqual(mail_record, searched_record)

    def test_userdir_searchInvalid(self):
        d = UserDirectory()
        self.assertEqual(None, d.searchForRecord(55, "Invalid"))
    
if __name__ == "__main__":
    unittest.main()