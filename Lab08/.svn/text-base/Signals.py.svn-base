from moduleTasks import *

def loadMultiple(signalNames, folderName, maxCount):
    result = dict()
    for i in range(len(signalNames)):
        signalName = signalNames[i]
        try:
            data = loadDataFrom(signalName, folderName)
        except:
            data = (None, maxCount-1)

        if data[1] < maxCount:
            result[signalName] = data[0]
        else:
            temp = list()
            result[signalName] = temp

    return result

def saveData(signalsDictionary, targetFolder, bounds, threshold):
    for signalName, signalData in signalsDictionary.items():
        if signalData is None or len(signalData) == 0: # len == 0 : The file is present but has too many invalid entries
            continue                                   # signalData is None: The file is not present int he folder

        if isBounded(signalData, bounds, threshold):
            dir = targetFolder + "/" + signalName + ".txt"
            with open(dir, "a+") as fileName:
                for num in signalData:
                    fileName.write("{0:.3f}".format(num)+"\n")

# lims = (-100, 100)
# x = loadMultiple(["AFW-481"], "Signals", 100)
# saveData(x, "Results", lims, 100)