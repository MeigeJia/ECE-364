import re
def getUrlParts(url):
    x = re.search("^http://(?P<BaseAddress>.+?)/(?P<Controller>.+?)/(?P<Action>.+?)\?", url)
    return [x.group("BaseAddress"), x.group("Controller"), x.group("Action")]

def getSpecial(sentence, letter):
    words = re.findall("\w+", sentence)
    result = list()
    for word in words:
        if re.match("^"+letter+"\w*"+"[^"+letter+"]"+"$", word, re.I) is not None:
            result.append(word)
        elif re.match("^[^"+letter+"]"+"\w*"+letter+"$", word, re.I) is not None:
            result.append(word)
    return result

def getState(fn):
    result = list()
    with open(fn, "r") as fp:
        for line in fp:
            state = re.search(",([\w\s]+)\n$", line)
            if state is None:
                result.append(None)
            else:
                result.append(state.group(1))
    return result

# print(getState("Employees.txt"))


###################### PART 1 #############################
# url = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
# print(getUrlParts(url))
# print(getQueryParameters(url))
# s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
# print(getSpecial(s, "t"))
# s = "supsupsup58:1C:0A:6E:39:4Dsupsupsup"
# print(getRealMAC(s))