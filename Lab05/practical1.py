def getFreeByNames(names):

    count = 1
    result = dict()
    for x in names:
        with open("Availability.txt", 'r') as myFile:
            for line in myFile:
                if count < 4:
                    count = count+1
                    continue

                data = line.split()
                try:
                    fname = data[0]
                    lname = data[1]
                except:
                    continue

                dates = list()
                name = fname+ " " + lname


                for i in range(3, len(data), 2):
                    dates.append(data[i])


                temp = list()
                if(name == x):
                    for y in range(len(dates)):
                        if int(dates[y]) == 1:
                            curList = result.get(name, temp)

                            if len(str(y+1)) == 1:
                                date = "08/0"+str(y+1)
                            else:
                                date = "08/"+str(y+1)

                            curList.append(date)
                            result[name] = curList

    return result

def getFreeRange(date1, date2):
    count = 1
    result = dict()

    with open("Availability.txt", 'r') as myFile:
        for line in myFile:
            if count < 4:
                count = count+1
                continue

            data = line.split()
            try:
                fname = data[0]
                lname = data[1]
            except:
                continue

            dates = list()
            name = fname+ " " + lname


            for i in range(3, len(data), 2):
                dates.append(data[i])

            result[name] = dates

    day1 = int(date1[3:5])
    day2 = int(date2[3:5])

    people = set()

    for i,j in result.items():
        put = 1
        for m in range(day1, day2):
            if(j[m] != "1"):
                put = 0
        if(put == 1):
            people.add(i)

    return people

def getStateByCounty(county):
    count=1
    countyToLat = dict()
    latToZip = dict()
    with open("Counties.txt", 'r') as myFile:
        for line in myFile:
            if count < 3:
                count = count+1
                continue
            data = line.split()
            countyToLat[data[2]] = (data[0], data[1])

    with open("LatLong.txt", 'r') as myFile:
        for line in myFile:
            if count < 3:
                count = count+1
                continue
            data = line.split()
            try:
                latToZip[data[2]] = (data[0], data[1])
            except:
                continue

    zipToState = dict()
    with open("ZipCodes.txt", 'r') as myFile:
        for line in myFile:
            if count < 3:
                count = count+1
                continue
            data = line.split()
            try:
                zipToState[data[2]] = (data[0], data[1])
            except:
                continue

    return zipToState[latToZip[countyToLat[county]]]



getStateByCounty("")