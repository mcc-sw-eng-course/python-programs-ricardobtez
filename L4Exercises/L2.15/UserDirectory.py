"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

L2 - 15
Create a class to manage a directory of users containing data
- Name
- Address
- Phone
- Email
The class must be enable:
- Creation of new record
- Save all records in a file
- Load records from a file
- Search and get data from a given record
"""

from enum import Enum

class UserDataType(Enum):
    NAME    = "name"
    ADDRESS = "address"
    PHONE   = "phone"
    MAIL    = "mail"

class UserDirectory():
    def __init__(self):
        self.m_directory = []
        return None

# Add a new User to our Directory
    def addRecord(self, name, address, phone, mail):
        record = {
            UserDataType.NAME : name,
            UserDataType.ADDRESS : address,
            UserDataType.PHONE : phone,
            UserDataType.MAIL : mail
        }
        self.m_directory.append(record)

# Saves the complete Directory to the given file
    def saveDirectoryToFile(self, filename):
        if isinstance(filename, str):
            with open(filename, "w") as my_file:
                for record in self.m_directory:
                    new_record = ( 
                        f"{{ "
                        f"{UserDataType.NAME} : \"{record[UserDataType.NAME]}\","
                        f"{UserDataType.ADDRESS} : \"{record[UserDataType.ADDRESS]}\","
                        f"{UserDataType.PHONE} : \"{record[UserDataType.PHONE]}\","
                        f"{UserDataType.MAIL} : \"{record[UserDataType.MAIL]}\""
                        f" }}\n"
                    )
                    my_file.write(new_record)
    
# Appends all the records found in the file to the current directory
    def readDirectoryFromFile(self, filename):
        if isinstance(filename, str):
            with open(filename, "r") as my_file:
                for line in my_file:
                    self.m_directory.append(eval(line))

# searchs for a record, given the name and the data to search
    def searchForRecord(self, data_type: UserDataType, data: str):
        if isinstance(data_type, UserDataType):
            for record in self.m_directory:
                if record[data_type] == data:
                    return record
        else:
            return None