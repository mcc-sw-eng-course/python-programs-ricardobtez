"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

L2 - 10 - 14
Create a class called myPowerList, implement methods for:
- Adding an item
- Removing the n-th item
- Sort the list (without using list.sort())
- Lmerge(merge the list as prefix)
- Rmerge(merge the list as sufix)
- saveToTextFile(filename)
- readFromTextFile(filename)
"""

class myPowerList():
    def __init__(self):
        self.m_list = []

# Adds an integer item to the list
    def addItem(self, new_element):
        if isinstance(new_element, int):
            self.m_list.append(new_element)

#a Removes an index from the list, index start in 0
    def removeItem(self, index_to_remove):
        if isinstance(index_to_remove, int):
            if index_to_remove >= 0 and index_to_remove < len(self.m_list):
                self.m_list.pop(index_to_remove)

# Returns a a new list that is sorted using bubble sort
    def sortList(self):
        new_list = self.m_list.copy()
        list_len = len(new_list)
        
        for i in range(list_len):
            for j in range(0, list_len-i-1):
                if new_list[j] > new_list[j+1]:
                    new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
        return new_list

# Merge a list to the left
    def Lmerge(self, left_list):
        if isinstance(left_list, list):
            if all(isinstance(x, int) for x in left_list):
                self.m_list = left_list + self.m_list

# Merge a list to the right
    def Rmerge(self, right_list):
        if isinstance(right_list, list):
            if all(isinstance(x, int) for x in right_list):
                self.m_list = self.m_list + right_list

# Save the current list to a file
    def saveToTextFile(self, filename):
        if isinstance(filename, str):
            with open(filename, "w") as my_file:
                for item in self.m_list:
                    my_file.write("%s\n" % str(item))

# Save the current list to a file
    def readFromTextFile(self, filename):
        if isinstance(filename, str):
            with open(filename, "r") as my_file:
                for line in my_file:
                    new_item = int(line)
                    self.addItem(new_item)
