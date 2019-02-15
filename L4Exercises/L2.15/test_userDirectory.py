import unittest
from UserDirectory import *

class MyPowerListTestCases(unittest.TestCase):

    def test_addRecord(self):
        d = UserDirectory()
        d.addRecord("Sam", "Calle Falsa", "1234567", "sam@sam.com")
        d.addRecord("Pepe", "Calle 123", "789456", "peps@pepito.com")
        self.assertEqual(2, len(d.m_directory))

    def test_save_read_file(self):
        d1 = UserDirectory()
        d1.addRecord("Sam", "Calle Falsa", "1234567", "sam@sam.com")
        d1.addRecord("Pepe", "Calle 123", "789456", "peps@pepito.com")
        d1.saveDirectoryToFile("myTestDir.txt")
        d2 = UserDirectory()
        d2.readDirectoryFromFile("myTestDir.txt")
        self.assertListEqual(d1.m_directory, d2.m_directory)

    def test_search(self):
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

        # find by phone
        searched_record = d.searchForRecord(UserDataType.PHONE, "134679")
        self.assertDictEqual(phone_record, searched_record)

        # find by mail
        searched_record = d.searchForRecord(UserDataType.MAIL, "perla@facebook.com")
        self.assertDictEqual(mail_record, searched_record)



if __name__ == '__main__':
    unittest.main()