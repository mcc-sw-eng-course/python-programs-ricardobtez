import unittest
from myPowerList import myPowerList

class MyPowerListTestCases(unittest.TestCase):

    def test_addItem(self):
        my_list = myPowerList()
        my_list.addItem(5)
        self.assertEqual(1, len(my_list.m_list))

    def test_removeItem(self):
        my_list = myPowerList()
        my_list.addItem(5)
        my_list.addItem(6)
        my_list.addItem(7)
        my_list.removeItem(1)
        self.assertEqual([5,7], my_list.m_list)

    def test_sortList(self):
        my_list = myPowerList()
        my_list.addItem(6)
        my_list.addItem(7)
        my_list.addItem(10)
        my_list.addItem(1)
        my_list.addItem(5)
        self.assertEqual([1,5,6,7,10], my_list.sortList())

    def test_left_merge(self):
        my_list = myPowerList()
        my_list.addItem(5)
        my_list.Lmerge([1,2,3,4])
        self.assertEqual([1,2,3,4,5], my_list.m_list)

    def test_right_merge(self):
        my_list = myPowerList()
        my_list.addItem(5)
        my_list.Rmerge([1,2,3,4])
        self.assertEqual([5,1,2,3,4], my_list.m_list)


if __name__ == '__main__':
    unittest.main()