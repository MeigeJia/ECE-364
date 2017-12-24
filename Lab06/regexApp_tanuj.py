import re


def getUrlParts(url):
    query = r"(?:/)(?P<url>\w+\.\w+\.\w+)(?:/)(?P<control>.*)(?:/)(?P<action>\w+)(?:\?)"
    found = re.search(query, url)
    url = found.group('url')
    control = found.group('control')
    action = found.group('action')
    return((url,control,action))


def getQueryParameters(url):
    found = re.search(r"(?:\?)(.*)$", url)
    return re.findall(r"(\w+)=([^&]+)&", found.group(1) + "&")


def getSpecial(sentence, letter):
    start = re.findall(" (" + letter + "\w*)", " "+sentence + " ", re.I)
    end = re.findall("(\w*" + letter + ") ", " "+sentence + " ", re.I)
    both = [i for i in start if i not in end]
    both.extend([j for j in end if j not in start])

    return both


def getRealMAC(sentence):
    query = r"([a-zA-Z0-9]){2}(-|:)([a-zA-Z0-9]){2}(-|:)([a-zA-Z0-9]){2}(-|:)([a-zA-Z0-9]){2}(-|:)([a-zA-Z0-9]){2}(-|:)([a-zA-Z0-9]){2}"
    found = re.search(query,sentence)
    return found.group(0)


def getData():
    data = {}
    nameFL = r"^(?P<first>\w+) (?P<last>\w+)(?P<data>.*$)"
    nameLF = r"^(?P<last>\w+), (?P<first>\w+)(?P<data>.*$)"
    with open("Employees.txt") as fh:
        for line in fh:
            if re.search(nameFL,line):
                found = re.search(nameFL, line)
            elif re.search(nameLF, line):
                found = re.search(nameLF, line)
            else:
                raise Exception("ISSUE")
            data["{} {}".format(found.group("first"), found.group("last"))] = found.group("data")

    return data


def getRejectedEntries():
    rejects = [name for name, data in getData().items() if not any(a for a in re.sub(r"[,; ]+", "", data))]
    rejects.sort()
    return rejects


def getEmployeesWithIDs():
    employs = {}
    getid = r"([a-zA-Z0-9]{8}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{12})"
    for name, data in getData().items():
        id = re.search(getid, data)
        if id:
            id = str(id.group(0)).lower()
            if len(id) < 33:
                id = id[0:8] + "-" + id[8:12] + "-" + id[12:16] + "-" + id[16:20] + "-" + id[20:32]
            employs[name] = id
    return employs


def getEmployeesWithoutIDs():
    rejects = getRejectedEntries()
    ids = getEmployeesWithIDs()
    noid = []
    for name, data in getData().items():
        if name in rejects:
            continue
        if name not in ids:
            noid.append(name)
    noid.sort()
    return noid


def getEmployeesWithPhones():
    employs = {}
    getnum = r"\(?\d{3}\)?[ -]?\d{3}-?\d{4}"
    for name, data in getData().items():
        num = re.search(getnum, data)
        if num:
            num = re.sub(r"[\(\) -]", "", num.group(0))
            num = "({}) {}-{}".format(num[0:3], num[3:6], num[6:10])
            employs[name] = num
    return employs


def getEmployeesWithStates():
    employs = {}
    getstate = r"[a-zA-Z ]*$"
    for name, data in getData().items():
        num = re.search(getstate, data)
        if num and num.group(0):
            employs[name] = num.group(0)
    return employs


def getCompleteEntries():
    employs = {}
    states = getEmployeesWithStates()
    ids = getEmployeesWithIDs()
    nums = getEmployeesWithPhones()

    for name, data in getData().items():
        if name not in states or name not in ids or name not in nums:
            continue
        employs[name] = (ids[name], nums[name], states[name])

    return employs


print(getRejectedEntries())
x = getEmployeesWithIDs()
print(x)
print(len(x))
print("----")
x = getEmployeesWithoutIDs()
print(x)
print(len(x))
x = getEmployeesWithPhones()
print(x)
print(len(x))
x = getEmployeesWithStates()
print(x)
print(len(x))
x = getCompleteEntries()
print(x)
print(len(x))
