import os
def getRegistration():
    path = 'Classes'
    classList = dict()
    for fileName in os.listdir(path):
        className = fileName.split(".")[0]
        students = list()

        with open(path + "/" + fileName, 'r') as myFile:
            for line in myFile:
                name = line.strip()
                students.append(name)


        for student in students:
            x = list()
            temp = classList.get(student, x)
            temp.append(className)
            classList[student] = temp

    return classList

def getCommonClasses(studentName1, studentName2):
    registrations = getRegistration()
    try:
        student1classes = registrations[studentName1]
        student2classes = registrations[studentName2]
    except:
        return None
    common = set()
    for classNum in student1classes:
        if classNum in student2classes:
            common.add(classNum)

    return common
