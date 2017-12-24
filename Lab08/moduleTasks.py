def checkNetwork(**kwargs):
    import sys
    try:
        from exModule import runNetworkCode
        runNetworkCode(**kwargs)
    except ConnectionError as e:
        raise ConnectionError(e)
    except OSError as e:
        return "An issue encountered during runtime. The name of the error is: "+type(e).__name__
    else:
        return False
    return True

def isOk(signal):
    import re
    if re.search("^[A-Z]{3}-[0-9]{3}$", signal) is not None:
        return True
    return False

def loadDataFrom(signalName, folderName):

    if not isOk(signalName):
        raise ValueError(signalName+" is invalid.")

    try:
        floatList = list()
        wordCount = 0
        dir = folderName + "/" + signalName + ".txt"
        with open(dir, "r") as file:
            for line in file:
                cur = line.strip()
                try:
                    num = float(cur)
                    floatList.append(num)
                except:
                    wordCount += 1
    except:
        raise OSError(signalName+" not found in "+folderName)

    return (floatList, wordCount)

def isBounded(signalValues, bonds, threshold):
    count = 0
    lower = min(bonds[0], bonds[1])
    upper = max(bonds[0], bonds[1])

    if len(signalValues) == 0:
        raise ValueError("Signal contains no data.")

    for num in signalValues:
        if not(lower < num < upper):
            count += 1

        if count > threshold:
            return False
    return True




# print(checkNetwork())
# print(isOk("DEF-12gg"))
# print(loadDataFrom("HQP-689", "Signals"))