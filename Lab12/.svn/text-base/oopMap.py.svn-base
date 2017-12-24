class Entry:
    def __init__(self, k=0, v=""):
        if type(k) != int:
            raise TypeError("Key MUST be of type 'int'!")
        if type(v) != str:
            raise TypeError("Key MUST be of type 'str'!")

        self.key = k
        self.value = v

    def __str__(self):
        return "("+str(self.key) + ': "' + self.value + '")'

    def __hash__(self):
        t = (self.key, self.value)
        return hash(t)

class Lookup:
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("Name cannot be empty!")

        self._name = name
        self._entrySet = set()

    def __str__(self):
        numEntries = len(self._entrySet)
        if numEntries >= 10:
            return'["' + self._name + '": ' + str(numEntries) + ' Entries]'
        else:
            return'["' + self._name + '": 0' + str(numEntries) + ' Entries]'

    def addEntry(self, entry):
        for e in self._entrySet:
            if(e.key == entry.key):
                raise ValueError("This key already exists! Please enter a new key.")

        temp = list(self._entrySet)
        temp.append(entry)
        self._entrySet = set(temp)

    def removeEntry(self, entry):
        found = 0
        for e in self._entrySet:
            if(e.key == entry.key):
                found = 1
        if not found:
            raise ValueError("This key does not exist!")

        temp = list(self._entrySet)
        temp.remove(entry)
        self._entrySet = set(temp)

    def getEntry(self, key):
        for e in self._entrySet:
            if(e.key == key):
                return e
        raise KeyError("This key does not exist!")

    def getAsDictionary(self):
        result = dict()
        for e in self._entrySet:
            result[e.key] = e.value
        return result

################## TESTING ##################
# print("\n------------------------------------------------------------------\n")
#
# y = Lookup("NAMES")
# print(y)
#
# x = Entry(1, "Gautam")
# print(x)
#
# a = Entry(2, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# a = Entry(3, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# a = Entry(4, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# a = Entry(5, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# a = Entry(6, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# a = Entry(7, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# a = Entry(8, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# a = Entry(9, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# a = Entry(10, "Ravi")
# print(a)
#
# y.addEntry(a)
# print(y)
#
# y.addEntry(x)
# print(y)
#
# y.removeEntry(x)
# print(y)
#
# b = y.getEntry(7)
# print(b)
#
# dictionary = y.getAsDictionary()
# print(dictionary)
#



