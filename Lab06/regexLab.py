def parseXML(xmlNode):
    import re
    query = r"([a-z]+)=\"([\w\s]+)\""
    attributes = re.findall(query, xmlNode)
    attributes.sort()
    return attributes

def tupleToString(x):
    for i in x:
        if i != "":
            return i
    return None


def captureNumbers(sentence):
    import re

    query1 = r"^([+-]?[0-9]{1}[\.][0-9]+[eE][+-]?[0-9]+)[\s\.\,]"
    query2 = r"^([+-]?[0-9]+[\.][0-9]+)[\s\.\,]"
    query3 = r"^([+-]?[0-9]+)[\s\.\,]"
    query4 = r"[\s]([+-]?[0-9]{1}[\.][0-9]+[eE][+-]?[0-9]+)[\s\.\,]"
    query5 = r"[\s]([+-]?[0-9]+[\.][0-9]+)[\s\.\,]"
    query6 = r"[\s]([+-]?[0-9]+)[\s\.\,]"

    nums = re.findall(query1+"|"+query2+"|"+query3+"|"+query4+"|"+query5+"|"+query6, sentence)

    result = list()
    for i in nums:
        temp = tupleToString(i)
        result.append(temp)

    return result


# def captureNumbers(sentence):
#     import re
#
#     query1 = r"[^\w]([+-]?[0-9]+[.]?[0-9]+[eE]?[+-]?[0-9]+[\.]?[0-9]+)[^\w]"
#     query2 = r"[^\w]([+-]?[0-9]+[eE]?[+-]?[0-9]+[.]?[0-9]+)[^\w]"
#     query3 = r"[^\w]([+-]?[0-9]+[.]?[0-9]+[eE]?[+-]?[0-9]+)[^\w]"
#     query4 = r"[^\w]([+-]?[0-9]+[eE]?[+-]?[0-9]+)[^\w]"
#     query5 = r"[^\w]([+-]?[0-9]+[.]?[0-9]+)[^\w]"
#     query6 = r"[^\w]([+-]?[0-9]+)[^\w]"
#
#
#     nums = re.findall(query1+"|"+query2+"|"+query3+"|"+query4+"|"+query5+"|"+query6, sentence)
#
#
#     result = list()
#     for i in nums:
#         temp = tupleToString(i)
#         result.append(temp)
#
#     print(result)

# xmlNode = '<person  name="Irene Adler" gender="female"  age="35"'
# print(parseXML(xmlNode))
#
# s = "444 With the electron's charge being -1.6022e-19, some ch666oices  you have are -110, -32.0 and +55. Assume that pi ++++7 equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+23."
# print(captureNumbers(s))