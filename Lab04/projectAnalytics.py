import os

################################ USER DEFINED FUNCTIONS ###############################
def getStudentsAndIds():
    namesAndIds = dict()
    with open("students.txt", 'r') as myFile:
        for line in myFile:
            temp = line.split()
            if(len(temp) < 3):
                continue

            fname = temp[1]     # includes comma at the end
            lname = temp[0]
            name = lname + " " + fname
            id = temp[3]
            namesAndIds[name] = id

    return namesAndIds

def getCircuitsAndProjects(circOrProj, mode):
    projsAndCircuits = list()
    with open("projects.txt", 'r') as myFile:
        for line in myFile:
            temp = line.split()
            if(len(temp) < 2):
                continue

            projectID = temp[1]
            circuitNum = temp[0]
            if(mode == "c"):   #given circuit num find projects
                if(circuitNum == circOrProj):
                    projsAndCircuits.append(projectID)
            elif(mode == "p"):
                if(projectID == circOrProj):
                    projsAndCircuits.append(circuitNum)

    return projsAndCircuits     # Each circuit maps to a project

def findStudentsCircuits(cur_id):
    path = 'Circuits'
    circuits = list()
    for filename in os.listdir(path):
        circuit = filename[filename.find("_")+1: filename.find(".")]
        if cur_id in getStudentsInCircuit(circuit):
            circuits.append(circuit)

    return circuits

def getStudentsInCircuit(circuitNum):       # returns a list of student ids
    fileName = "circuit_" + circuitNum + ".txt"
    rel_dir = "Circuits/"+fileName
    with open(rel_dir, 'r') as myFile:
        for i, line in enumerate(myFile):
            if(i == 1):
                participants = line
                break

    participants = participants.split(", ")
    for i in range(len(participants)):
        id = participants[i]
        id = id[0:11]
        participants[i] = id
    return participants


def getComponentsInCircuit(circuitNum):
    components = list()
    compFreq = dict()
    fileName = "circuit_" + circuitNum + ".txt"
    rel_dir = "Circuits/"+fileName
    with open(rel_dir, 'r') as myFile:
        for line in myFile:
            lastLine = line

        components = lastLine.split(", ")

        for comp in components:
            type = comp[0]
            qty = 1 #comp[comp.find(".")+1:]
            compFreq[type] = compFreq.get(type, 0) + int(qty)

    return compFreq, components    # dict of the number of components in circuit

################################ ASSIGNMENT FUNCTIONS ###########################################

def getComponentCountByProject(projectID):
    circuits = getCircuitsAndProjects(projectID, "p")
    if(len(circuits) == 0):
        return None
    compFreq = dict()
    comp_list = list()
    for c in circuits:
        fileName = "circuit_" + c + ".txt"
        rel_dir = "Circuits/"+fileName


        with open(rel_dir, 'r') as myFile:
            for line in myFile:
                lastLine = line

        components = lastLine.split(", ")
        for comp in components:
            if comp not in comp_list:
                comp_list.append(comp)


    for comp in comp_list:
        type = comp[0]
        compFreq[type] = compFreq.get(type, 0) + 1


    result = (compFreq.get("R", 0), compFreq.get("L", 0), compFreq.get("C", 0), compFreq.get("T", 0))
    return result


def getComponentCountByStudent(studentName):
    studentsAndIds = getStudentsAndIds()
    try:
        cur_id = studentsAndIds[studentName]
    except:
        return None
    circuits = findStudentsCircuits(cur_id)
    if len(circuits) == 0:
        result = ()
        return result
    comp_list = list()

    compFreq = dict()
    for circuit in circuits:
        circuits_num = circuit[circuit.find("_")+1: circuit.find(".")]
        temp, comps = getComponentsInCircuit(circuits_num)
        for comp in comps:
            if comp not in comp_list:
                comp_list.append(comp)

    for comp in comp_list:
        type = comp[0]
        compFreq[type] = compFreq.get(type, 0) + 1

    result = (compFreq.get("R", 0), compFreq.get("L", 0), compFreq.get("C", 0), compFreq.get("T", 0))
    return result


def getParticipationByStudent(studentName):
    studentsAndIds = getStudentsAndIds()
    try:
        cur_id = studentsAndIds[studentName]
    except:
        return None

    circuits = findStudentsCircuits(cur_id)
    if len(circuits) == 0:
        result = ()
        return result
    projects = dict()
    for circuit in circuits:
        curCircProjs = getCircuitsAndProjects(circuit, "c")
        for proj in curCircProjs:
            projects[proj] = 1

    result = list()
    for p in projects.keys():
        result.append(p)

    return result

def getParticipationByProject(projectID):
    circuits = getCircuitsAndProjects(projectID, "p")
    if len(circuits) == 0:
        return None
    students = dict()
    for circuit in circuits:
        curStudents = getStudentsInCircuit(circuit)
        for s in curStudents:
            students[s] = 1

    studentNames = list()
    studentNamesAndIds = getStudentsAndIds()
    studentsIdsAndNames = {i: s for s, i in studentNamesAndIds.items()}
    for s in students.keys():
        studentNames.append(studentsIdsAndNames[s])

    return studentNames


def getProjectByComponent(components):

    results = dict()
    for comp in components:
        path = 'Circuits'
        circuits = list()
        for filename in os.listdir(path):
            circuit_num = filename[filename.find("_")+1: filename.find(".")]
            temp, curComps = getComponentsInCircuit(circuit_num)
            if comp in curComps:
                circuits.append(circuit_num)

        project = dict()
        for circuit in circuits:
            projects = getCircuitsAndProjects(circuit, "c")
            for p in projects:
                project[p] = 1

        projList = set()
        for p in project.keys():
            projList.add(p)

        results[comp] = projList

    return results


def getStudentByComponent(components):

    idsAndStudents = getStudentsAndIds()
    idsAndStudents = {i: s for s, i in idsAndStudents.items()}
    result = dict()

    for comp in components:
        path = 'Circuits'
        circuits = list()
        for filename in os.listdir(path):
            circuit_num = filename[filename.find("_")+1: filename.find(".")]
            temp, curComps = getComponentsInCircuit(circuit_num)
            if comp in curComps:
                circuits.append(circuit_num)

        nameList = set()
        for circuit in circuits:
            ids = getStudentsInCircuit(circuit)
            for id in ids:
                if idsAndStudents[id] not in nameList:
                    nameList.add(idsAndStudents[id])

        result[comp] = nameList

    return result

def getComponentByStudent(studentNames):
    studentsAndIds = getStudentsAndIds()
    studentsAndComps = dict()
    for student in studentNames:
        id = studentsAndIds[student]
        components = dict()
        circuits = findStudentsCircuits(id)
        for circuit in circuits:
            temp, comps = getComponentsInCircuit(circuit)
            for comp in comps:
                components[comp] = 1    # Check whether you need this -- might not need a dict

        compList = set()
        for comp in components.keys():
            compList.add(comp)

        studentsAndComps[student] = compList

    return studentsAndComps


def getCommonByProject(projectID1, projectID2):
    proj1_circuits = getCircuitsAndProjects(projectID1, "p")
    proj2_circuits = getCircuitsAndProjects(projectID2, "p")
    if(len(proj1_circuits) == 0 or len(proj2_circuits) == 0):
        return None
    proj1_comps = dict()
    proj2_comps = dict()
    for circuit in proj1_circuits:
        temp, comps = getComponentsInCircuit(circuit)
        for comp in comps:
            proj1_comps[comp] = 1
    proj1_compList = list()
    for comp in proj1_comps.keys():
        proj1_compList.append(comp)

    for circuit in proj2_circuits:
        temp, comps = getComponentsInCircuit(circuit)
        for comp in comps:
            proj2_comps[comp] = 1
    proj2_compList = list()
    for comp in proj2_comps.keys():
        proj2_compList.append(comp)

    common = list()
    for comp in proj1_compList:
        if comp in proj2_compList:
            common.append(comp)

    common.sort()
    if len(common) == 0:
        return None
    return common


def getCommonByStudent(studentName1, studentName2):
    studentsAndIds = getStudentsAndIds()

    try:
        id1 = studentsAndIds[studentName1]
        id2 = studentsAndIds[studentName2]
    except:
        return None

    stud1_circuits = findStudentsCircuits(id1)
    stud2_circuits = findStudentsCircuits(id2)
    if(len(stud1_circuits) == 0 or len(stud2_circuits) == 0):
        return None
    stud1_comps = dict()
    stud2_comps = dict()
    for circuit in stud1_circuits:
        temp, comps = getComponentsInCircuit(circuit)
        for comp in comps:
            stud1_comps[comp] = 1
    stud1_compList = list()
    for comp in stud1_comps.keys():
        stud1_compList.append(comp)

    for circuit in stud2_circuits:
        temp, comps = getComponentsInCircuit(circuit)
        for comp in comps:
            stud2_comps[comp] = 1
    proj2_compList = list()
    for comp in stud2_comps.keys():
        proj2_compList.append(comp)

    common = list()
    for comp in stud1_compList:
        if comp in proj2_compList:
            common.append(comp)

    common.sort()
    if len(common) == 0:
        return None
    return common


def getProjectByCircuit():
    path = 'Circuits'
    result = dict()
    for filename in os.listdir(path):
        circuit_num = filename[filename.find("_")+1: filename.find(".")]
        projs = getCircuitsAndProjects(circuit_num, "c")
        projs.sort()
        result[circuit_num] = projs

    return result

def getCircuitByStudent():
    studentsAndIds = getStudentsAndIds()
    results = dict()
    for st, id in studentsAndIds.items():
        if st == "Last, First":
            continue
        circuits = findStudentsCircuits(id)
        for i in range(len(circuits)):
            temp = circuits[i]
            circuits[i] = temp[temp.find("_")+1: temp.find(".")]
        results[st] = circuits

    return results

def getCircuitByStudentPartial(studentName):
    studentsAndIds = getStudentsAndIds()
    students = list()
    for st in studentsAndIds.keys():
        students.append(st)

    studentsAndCircuits = getCircuitByStudent()
    result = dict()

    for st in students:
        [lname, fname] = st.split(", ")
        if(lname == studentName or fname == studentName):
            name = lname + ", " + fname
            result[name] = studentsAndCircuits[name]
    if len(result) == 0:
        return None
    return result
# print("QUESTION 1")
print(getComponentCountByProject("D230BAC0-249C-410F-84E4-41F9EDBFCB20"))
#
# print("QUESTION 2")
# print(getComponentCountByStudent("--"))
#
# print("QUESTION 3")
# x = getParticipationByStudent("Young, Frank")   #Need to add code for when student name doesnt exist
# print(len(x))
#
# print("QUESTION 4")
# x = getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
# print(len(x))
#
# print("QUESTION 5")
# x = getProjectByComponent(["T39.201", "T489.263"])
# print(x)
#
# print("QUESTION 6")
# x = getStudentByComponent(["T39.201", "T71.386"])
# print(x)
# for i in x.values():
#     print(len(i))
#
# print("QUESTION 7")
# x = getComponentByStudent(["Allen, Amanda", "Adams, Keith"]) # Check whether its only unique elements or if its all components
# print(x)
# for i in x.values():
#      print(len(i))
#
# print("QUESTION 8")
# x = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "90BE0D09-1438-414A-A38B-8309A49C02EF")
# print(x)
# print(len(x))
#
# print("QUESTION 9")
# x = getCommonByStudent("Allen, Amanda", "Adams, Keith")
# print(x)
# print(len(x))
#
# print("QUESTION 10")
# print(getProjectByCircuit())
#
# print("QUESTION 11")
print(getCircuitByStudent())
#
# print("QUESTION 12")
print(getCircuitByStudentPartial("Scott"))
