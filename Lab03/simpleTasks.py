def find(pattern):
    with open('sequence.txt', 'r') as myFile:
        content = myFile.read()

    m = len(pattern)
    n = len(content)
    results = list()

    for i in range(n):
        str = content[i : i+m]
        if(len(str) < m):
            break

        found = 1
        for j in range(m):
            if((pattern[j] != "X") and (str[j] != pattern[j])):
                found = 0

        if(found == 1):
            results.append(str)

    return results

def getStreakProduct(sequence, maxSize, product):
    results = list()

    for i in range(len(sequence)):
        for j in range(2, maxSize+1):
            curSeq = sequence[i:i+j]
            curProd = 1
            for num in curSeq:
                curProd = curProd * int(num)
            if (curProd == product):
                results.append(curSeq)

    return results

def writePyramids(filePath, baseSize, count, char):
    open(filePath, 'w').close()

    for curBase in range(1, baseSize+1, 2):
        for pyramidNum in range(count):
            for preSpaces in range((baseSize-curBase)//2):
                with open(filePath, "a") as myfile:
                    myfile.write(" ")

            for charNum in range(curBase):
                with open(filePath, "a") as myfile:
                    myfile.write(char)

            for postSpaces in range((baseSize-curBase+2)//2):
                with open(filePath, "a") as myfile:
                    myfile.write(" ")

        with open(filePath, "a") as myfile:
            myfile.write("\n")

    return

def getStreaks(sequence, letters):
    letterList = list()
    for letter in letters:
        letterList.append(letter)

    i = 0
    j = 0
    result = list()
    while (i < len(sequence)):
        if(sequence[i] in letterList):
            j = i
            while(sequence[j] == sequence[i]):
                j = j+1
                if(j >= len(sequence)):
                    break

            str = sequence[i:j]
            result.append(str)
            i = j
            j = 0
        else:
            i = i+1

    return result


def findNames(nameList, part, name):
    results = list()
    for person in nameList:
        [fname, lname] = person.split(" ")
        if (part == "F"):
            if(fname.lower() == name.lower()):
                results.append(person)
        elif (part == "L"):
            if(lname.lower() == name.lower()):
                results.append(person)
        elif (part == "FL"):
            if(fname.lower() == name.lower()):
                results.append(person)
            if(lname.lower() == name.lower()):
                results.append(person)

    return results


def convertToBoolean(num, size):
    binNum = bin(num)
    binNum = binNum[2:]
    results = list()
    padNum = size - len(binNum)

    if (padNum < 0):
        padNum = 0
    for i in range(padNum):
        results.append(False)

    for i in binNum:
        if(int(i) == 0):
            results.append(False)
        elif(int(i) == 1):
            results.append(True)

    return results


def convertToInteger(boolList):
    binNum = ""
    for element in boolList:
        if(element == False):
            binNum+="0"
        elif(element == True):
            binNum+="1"

    result = int(binNum, 2)
    return result


# Problem1 - Find Pattern
#results = find("1XX7")

# Problem 2 - Get Streaks Product
#results = getStreakProduct("14822", 3, 32)

# Problem 3 - Write Pyramids
writePyramids('pyramid13.txt', 21, 7, '#')

# Problem 4 - Get Streaks
#sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
#results = getStreaks(sequence, "SAQBT")

# Problem 5 - Find Names
#names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
#results = findNames(names, "FL", "johnson")

# Problem 6 - Convert To Boolean
#results = convertToBoolean(9, 3)

# Problem 7 - Convert To Integer
#bList = [False, True, False, True, False, False, True]
#results = convertToInteger(bList)

#print(results)
