def validComp(compList,compType):
    import re
    if len(compList) > 0:
        for comp in compList:
            if re.search("^"+compType.upper()+"[\d]+[\.][\d]+$",comp) is None:
                return 0
    return 1

####################### PROJECT FUNCTIONS ########################

from enum import Enum
class Level(Enum):
    freshman = 1
    sophomore = 2
    junior = 3
    senior = 4


class Student:
    def __init__(self, id, fn, ln, lvl):
        if (len(id) != 11):
            raise TypeError("ID must be in the format 'XXXXX-XXXXX'")
        if (type(lvl) != Level):
            raise TypeError("The argument must be an instance of the 'Level' Enum.")
        self.ID = id
        self.firstName = fn
        self.lastName = ln
        self.level = lvl

    def __str__(self):
        return "{}, {} {}, {}".format(self.ID, self.firstName, self.lastName, self.level.name.title())

class Circuit:

    def __init__(self, id, r_list, c_list, l_list, t_list):

        # Check if components are all valid
        if not validComp(r_list, "R"):
            raise ValueError("The resistors' list contain invalid components.")
        if not validComp(c_list, "C"):
            raise ValueError("The resistors' list contain invalid components.")
        if not validComp(l_list, "L"):
            raise ValueError("The resistors' list contain invalid components.")
        if not validComp(t_list, "T"):
            raise ValueError("The resistors' list contain invalid components.")
        if len(id) != 5:
            raise ValueError("The circuit ID must be exactly 5 digits long.")

        self.ID = id
        self.resistors = r_list
        self.capacitors = c_list
        self.inductors = l_list
        self.transistors = t_list

    def __str__(self):
        ret_str = "" + self.ID + ": (R = %02d" % len(self.resistors) + ", C = %02d" % len(self.capacitors)
        ret_str = ret_str + ", L = %02d" % len(self.inductors) + ", T = %02d" % len(self.transistors) + ")"
        return ret_str

    def getDetails(self):   ################################### Check the sorting later
        r_sorted = sorted(self.resistors)
        c_sorted = sorted(self.capacitors)
        l_sorted = sorted(self.inductors)
        t_sorted = sorted(self.transistors)
        ret_str = "" + self.ID + ": "
        for r in r_sorted:
            ret_str = ret_str + r + ", "
        for c in c_sorted:
            ret_str = ret_str + c + ", "
        for l in l_sorted:
            ret_str = ret_str + l + ", "
        for t in t_sorted:
            ret_str = ret_str + t + ", "
        return ret_str[:-2]

    def __contains__(self, comp):
        if (not isinstance(comp, str)):
            raise TypeError("Argument is not of type string")
        compTypes = ["R", "L", "T", "C"]
        if (comp == "" or comp[0] not in compTypes):
            raise ValueError("Component not of known type.")
        return comp in self.resistors or comp in self.capacitors or comp in self.inductors or comp in self.transistors

    def __add__(self, other):
        if type(other) == str:
            if other not in self:
                if (other[0] == "R"):
                    self.resistors.append(other)
                elif (other[0] == "C"):
                    self.capacitors.append(other)
                elif (other[0] == "L"):
                    self.inductors.append(other)
                elif (other[0] == "T"):
                    self.transistors.append(other)
            return self
        elif (type(other) == Circuit):
            from random import sample
            idNew = "".join([str(i) for i in sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)])
            rNew = list(set(self.resistors + other.resistors))
            cNew = list(set(self.capacitors + other.capacitors))
            iNew = list(set(self.inductors + other.inductors))
            tNew = list(set(self.transistors + other.transistors))
            newCircuit = Circuit(idNew, rNew, cNew, iNew, tNew)
            return newCircuit
        else:
            return TypeError("Operand is not of type String or Circuit.")

    def __sub__(self, other):
        if type(other) != str:
            raise TypeError("Operand is not of type string.")

        if other[0] == "R":
            if other in self.resistors:
                self.resistors.remove(other)
        elif other[0] == "L":
            if other in self.inductors:
                self.inductors.remove(other)
        elif other[0] == "C":
            if other in self.capacitors:
                self.capacitors.remove(other)
        elif other[0] == "T":
            if other in self.transistors:
                self.transistors.remove(other)
        else:
            raise ValueError("Component not of known type.")
        return self

class Project:
    def __init__(self, uuid, participants, circuits):
        if (len(participants) == 0 or not all([type(i) == Student for i in participants])):
            raise ValueError("Participants list is empty/invalid")

        if (len(circuits) == 0 or not all([type(i) == Circuit for i in circuits])):
            raise ValueError("Circuits list is empty/invalid")

        from uuid import UUID
        self.ID = str(UUID(uuid))
        self.participants = participants
        self.circuits = circuits

    def __str__(self):
        return self.ID + ": %02d Circuits, " % len(self.circuits) + "%02d Participants" % len(self.participants)

    def getDetails(self):
        sorted_participants = sorted(self.participants, key=lambda x: x.ID)
        sorted_circuits = sorted(self.circuits, key=lambda x: x.ID)

        ret_str = self.ID + "\n\n"
        ret_str = ret_str + "Participants:\n"
        for student in sorted_participants:
            ret_str = ret_str + student.__str__() + "\n"
        ret_str = ret_str + "\nCircuits:\n"
        for circuit in sorted_circuits:
            ret_str = ret_str + circuit.getDetails() + "\n"
        return ret_str

    def __contains__(self, item):
        if (type(item) == str):
            compTypes = ["R", "L", "T", "C"]
            if (item == "" or not item[0] in compTypes):
                raise ValueError("Component not of known type.")
            if any([item in circuit for circuit in self.circuits]):
                return True
            else:
                return False
        elif (type(item) == Circuit):
            if any([item.ID == circuit.ID for circuit in self.circuits]):
                return True
            else:
                return False
        elif (type(item) == Student):
            if any([item.ID == participant.ID for participant in self.participants]):
                return True
            else:
                return False
        else:
            raise TypeError("Item is not a component, student or circuit.")

    def __add__(self, other):
        if type(other) == Circuit:
            if not any([other.ID == circuit.ID for circuit in self.circuits]):
                self.circuits.append(other)
        elif type(other) == Student:
            if not any([other.ID == student.ID for student in self.participants]):
                self.participants.append(other)
        else:
            raise TypeError("Operand is not valid")
        return self

    def __sub__(self, other):
        if (type(other) == Circuit):
            if (other.ID == circuit.id for circuit in self.circuits):
                self.circuits.remove(other)
        elif (type(other) == Student):
            if (other.ID == student.ID for student in self.participants):
                self.participants.remove(other)
        else:
            raise TypeError("Item is not of Circuit class or Student class")
        return self


class Capstone(Project):

    def __init__(self, id, participants, circuits):
        from uuid import UUID
        if (len(participants) == 0):
            raise ValueError("Participants list is empty")
        if (any([type(student) != Student for student in participants])):
            raise ValueError("One or more members are not a part of student class.")
        if (len(circuits) == 0):
            raise ValueError("Circuits list is empty")
        if (any([type(circuit) != Circuit for circuit in circuits])):
            raise ValueError("One or more members are not a part of circuit class.")
        if (any([student.level != Level.senior for student in participants])):
            raise ValueError("One or more members are not a senior.")

        self.ID = str(UUID(id))
        self.participants = participants
        self.circuits = circuits

    def __add__(self, other):
        if (type(other) == Circuit):
            if all([other.ID != circuit.ID for circuit in self.circuits]):
                self.circuits.append(other)
            return self
        elif (type(other) == Student):
            if all([other.ID != student.ID for student in self.participants]):
                if (other.level == Level.senior):
                    self.participants.append(other)
                    return self
                else:
                    raise ValueError("Student to be added is not a Senior.")
        else:
            raise TypeError("Operand is not a student or a circuit.")
