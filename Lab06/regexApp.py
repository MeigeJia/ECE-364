import re

###################### PART 1 #############################

def getUrlParts(url):
    a = re.search("(http://)([\w.-_]+?)/([\w.-_]+?)/([\w.-_]+?)\?", url)
    result = (a.group(2), a.group(3), a.group(4))
    return result

def getQueryParameters(url):
    a = re.search("\?(.*)", url)
    a = a.group(1) + "&"
    result = re.findall("([\w]+)=([\w]+)&", a)
    return(result)


def getSpecial(sentence, letter):
    words = re.findall("\w+", sentence)
    result = list()
    for word in words:
        if re.match("^"+letter+"\w*"+"[^"+letter+"]"+"$", word, re.I) is not None:
            result.append(word)
        elif re.match("^[^"+letter+"]"+"\w*"+letter+"$", word, re.I) is not None:
            result.append(word)

    return result

def getRealMAC(sentence):
    a = re.search("(?P<MAC>[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2})", sentence)
    b = re.search("(?P<MAC>[a-fA-F0-9]{2}-[a-fA-F0-9]{2}-[a-fA-F0-9]{2}-[a-fA-F0-9]{2}-[a-fA-F0-9]{2}-[a-fA-F0-9]{2})", sentence)
    if a is None and b is None:
        return None
    elif a is None:
        return b.group("MAC")

    return a.group("MAC")


###################### PART 2 #############################


def lineData(line):
    [name1, name2] = getNames(line)
    id = getID(line)
    number = getNumber(line)
    state = getState(line)
    return name1, name2, id, number, state


def getNames(line):
    names1 = re.search(r"^([\w]+)[\s]{1}([\w]+)", line)
    names2 = re.search(r"^([\w]+), ([\w]+)", line)
    name = None

    if names1 is not None:
        name = [names1.group(1), names1.group(2)]
    elif names2 is not None:
        name = [names2.group(2), names2.group(1)]

    return name


def getID(line):
    query = r"[\{]?[A-Za-z0-9]{8}[-]?[A-Za-z0-9]{4}[-]?[A-Za-z0-9]{4}[-]?[A-Za-z0-9]{4}[-]?[A-Za-z0-9]{12}[}]?"
    id = re.search(query, line)
    if id is None:
        return None
    else:
        from uuid import UUID
        id = re.sub(r"[/{}-]", "", id.group(0))
        id = "{"+id+"}"
        id = str(UUID(id))
        return id

def getNumber(line):
    query = r",([\(]?[0-9]{3}[\)}?[-]?[\s]?[0-9]{3}[-]?[0-9]{4});"
    number = re.search(query, line)
    if number is not None:
        number = re.sub(r"[^0-9]", "", number.group(1))
        num = "("+number[0:3]+") "+number[3:6]+"-"+number[6:]
        return num
    else:
        return None

def getState(line):
    query = r",([A-Za-z\s]+?)$"
    state = re.search(query, line)
    state = state.group(1)

    if(state == "\n"):
        return None
    else:
        return state

def getRejectedEntries():
    results = list()
    with open("Employees.txt", "r") as myFile:
        for line in myFile:
            name1, name2, id, number, state = lineData(line)
            if name1 is not None and name2 is not None and id is None and number is None and state is None:
                name = name1+" "+name2
                results.append(name)

    results.sort()
    return results

def getEmployeesWithIDs():
    results = dict()
    with open("Employees.txt", "r") as myFile:
        for line in myFile:
            name1, name2, id, number, state = lineData(line)
            if name1 is not None and name2 is not None and id is not None:
                name = name1+" "+name2
                results[name] = id
    return results

def getEmployeesWithoutIDs():
    results = list()
    with open("Employees.txt", "r") as myFile:
        for line in myFile:
            name1, name2, id, number, state = lineData(line)
            if name1 is not None and name2 is not None and id is None and (number is not None or state is not None):
                name = name1+" "+name2
                results.append(name)

    results.sort()
    return results

def getEmployeesWithPhones():
    results = dict()
    with open("Employees.txt", "r") as myFile:
        for line in myFile:
            name1, name2, id, number, state = lineData(line)
            if name1 is not None and name2 is not None and number is not None:
                name = name1+" "+name2
                results[name] = number
    return results

def getEmployeesWithStates():
    results = dict()
    with open("Employees.txt", "r") as myFile:
        for line in myFile:
            name1, name2, id, number, state = lineData(line)
            if name1 is not None and name2 is not None and state is not None:
                name = name1+" "+name2
                results[name] = state
    return results

def getCompleteEntries():
    results = dict()
    with open("Employees.txt", "r") as myFile:
        for line in myFile:
            name1, name2, id, number, state = lineData(line)
            if name1 is not None and name2 is not None and id is not None and number is not None and state is not None:
                name = name1+" "+name2
                results[name] = (id, number, state)
    return results

# def getData():
#    with open("Employees.txt", "r") as myFile:
#        for line in myFile:
#            name1, name2 = getNames(line)
#            id = getID(line)
#            number = getNumber(line)
#            state = getState(line)
#            print(name1, name2, id, number, state)

###################### PART 1 #############################
# url = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
# print(getUrlParts(url))
# print(getQueryParameters(url))
# s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
# print(getSpecial(s, "t"))
# s = "supsupsup58:1C:0A:6E:39:4Dsupsupsup"
# print(getRealMAC(s))

###################### PART 2 #############################
# print(getRejectedEntries())
# x = getEmployeesWithIDs()
# print(x)
# print(len(x))
# x = getEmployeesWithoutIDs()
# print(x)
# print(len(x))
# x = getEmployeesWithPhones()
# print(x)
# print(len(x))
# x = getEmployeesWithStates()
# print(x)
# print(len(x))
# x = getCompleteEntries()
# print(x)
# print(len(x))
