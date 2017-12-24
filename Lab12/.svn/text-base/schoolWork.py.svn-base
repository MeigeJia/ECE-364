# This function will return the list of courses, and a dictionary containing name -> scores(list).
#  (scores list will include '-'s)
def readFile():
    fname = "university.txt"
    result = dict()
    students = list()
    with open(fname, "r") as fp:
        for i,line in enumerate(fp):
            if(i == 0):
                continue
            elif(i == 1):   # GET LIST OF COURSES
                courses = line.split()[2:]
            elif(i==2):
                continue
            else:           # GET STUDENTS AND THEIR GRADES
                curLine = line.split("|")
                name = curLine[0].strip()
                students.append(name)
                scores = curLine[1:]
                for j, score in enumerate(scores):
                    scores[j] = score.strip()
                result[name] = scores
    return courses, students, result

def getStudentInfo():
    result = dict()
    courses, students, studentGrades = readFile()
    for s in students:
        result[s] = list()
        grades = studentGrades[s]
        for i,grade in enumerate(grades):
            if(grade != "-"):
                result[s].append((courses[i], float(grade)))

    for student in students:
        result[student].sort(key = lambda x:x[0])

    return result

def getClassInfo():
    result = dict()
    courses, students, studentGrades = readFile()
    for courseNum,c in enumerate(courses):  # Course Number is not the course id. It is the index where the course
                                            # appears in the list of courses.
        result[c] = list()
        for s in students:
            grades = studentGrades[s]
            if(len(grades) > courseNum and grades[courseNum] != "-"):
                result[c].append((s, float(grades[courseNum])))

    for course in courses:
        result[course].sort(key = lambda x:x[0])

    return result

def getBestInCourse(course):
    course_data = getClassInfo()
    courseGrades = course_data[course]
    courseGrades.sort(key = lambda x:x[1])
    return courseGrades[-1]

def getCourseAverage(course):
    course_data = getClassInfo()
    cur_course_data = course_data[course]
    total = 0
    for studentANDgrade in cur_course_data:
        total += studentANDgrade[1]
    return round(total/len(cur_course_data), 2)

def readCourseHours():
    fname = "courses.txt"
    result = dict()
    with open(fname, "r") as fp:
        for i,line in enumerate(fp):
            if(i < 2):
                continue
            [course, hours] = line.split()
            result[course] = float(hours)
    return result

def getStudentGPA(name):
    course_hours = readCourseHours()
    student_info = getStudentInfo()
    student_info = student_info[name]

    total_GPApoints = 0
    total_credits = 0

    for course,grade in student_info:
        total_credits += course_hours[course]
        total_GPApoints += grade*course_hours[course]

    return round(total_GPApoints/total_credits, 2)

################## TESTING ##################
#
# courses, students, studentGrades = readFile()
#
# print("\n------------------------------------------------------------------\n")
#
# student_data = getStudentInfo()
# for student in students:
#     print(student, student_data[student])
#
# print("\n------------------------------------------------------------------\n")
#
# course_data = getClassInfo()
# for course in courses:
#     print(course, course_data[course])
#
# print("\n------------------------------------------------------------------\n")
#
# best = getBestInCourse("ECE388")
# print(best)
#
# print("\n------------------------------------------------------------------\n")
#
# avg = getCourseAverage("ECE344")
# print(avg)
#
# print("\n------------------------------------------------------------------\n")
#
# gpa = getStudentGPA("Melba Gist")
# print(gpa)
#
# print("\n------------------------------------------------------------------\n")
