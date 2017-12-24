def loadVectors(filename):
    from simpleVector import Vector
    result = list()
    with open(filename, "r") as myFile:
        for line in myFile:
            try:
                x = Vector(line)
                result.append(x)
            except:
                result.append(None)

    return result
