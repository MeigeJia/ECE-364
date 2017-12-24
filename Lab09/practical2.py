
def parseSimple(fileName):
    import re
    result = dict()
    with open(fileName, "r") as fp:
        for line in fp:
           x = re.search("\"([\w]+?)\"[\s]?:[\s]?\"(.+?)\"", line)
           if x is not None:
                result[x.group(1)] = x.group(2)

    return result


def parseLine(fileName):
    import re
    result = dict()
    with open(fileName, "r") as fp:
        for line in fp:
           x = re.findall("\"([\w]+?)\"[\s]?:[\s]?\"(.+?)\"[,]?", line)

    for item in x:
        result[item[0]] = item[1]

    return result


def parseComplex(fileName):
    import re
    result = dict()
    with open(fileName, "r") as fp:
        for line in fp:
            x = re.search("\"([\w]+?)\"[\s]?:[\s]?\"(.+?)\"|\"([\w]+?)\"[\s]?:[\s]?(true|false)|\"([\w]+?)\"[\s]?:[\s]?(-?[0-9]+\.[0-9]+|-?[0-9]+)", line)
            if x is not None:
                if(x.group(1) is not None):
                    result[x.group(1)] = x.group(2)
                elif (x.group(3) is not None):
                    result[x.group(3)] = x.group(4)
                elif (x.group(5) is not None):
                    result[x.group(5)] = x.group(6)

    return result



def parseComposite(fileName):
    import re
    result = dict()
    with open(fileName, "r") as fp:
        for line in fp:
            if "[" not in line:
                x = re.search("\"([\w]+?)\"[\s]?:[\s]?\"(.+?)\"|\"([\w]+?)\"[\s]?:[\s]?(true|false)|\"([\w]+?)\"[\s]?:[\s]?(-?[0-9]+\.[0-9]+|-?[0-9]+)", line)
                if x is not None:
                    if(x.group(1) is not None):
                        result[x.group(1)] = x.group(2)
                    elif (x.group(3) is not None):
                        result[x.group(3)] = x.group(4)
                    elif (x.group(5) is not None):
                        result[x.group(5)] = x.group(6)
            else:
                x = re.findall("\"(.+?)\"", line)
                result[x[0]] = x[1:]
    return result


print(parseComposite("composite.json"))
