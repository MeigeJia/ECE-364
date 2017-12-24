################### LEVEL 1 #########################

# def answers(s):
#     multiples = list()
#     for i in range(1, len(s)):
#         if(len(s)%i == 0):
#             multiples.append(i)
#     print(multiples)
#
#     max = 0
#     for i in multiples:
#         j = 0
#         temp = list()
#         while(j < len(s)):
#             temp.append(s[j:j+i])
#             j = j+i
#
#         flag = 0
#         for x in range(1,len(temp)):
#             if(temp[x] != temp[x-1]):
#                 flag = 1
#                 break
#
#         if(flag == 0):
#             max = len(temp)
#             break
#
#     return max
#
#
# s = "abcabcabcabcabcabc"
# print(answers(s))


################### LEVEL 2 #########################
#
# def answer(n, h):
#
#     maxNum = pow(2, h)-1
#     nums = list(range(1,maxNum+1))
#
#     results = list()
#     for num in n:
#         x, level = leftChildLevel(nums, num, h)
#         if level is None:
#             results.append(-1)
#         else:
#             results.append(level)
#     return results

def leftOrRight(num, ht):   # None means it is parent, 1 means left and 0 means right
    maxNum = pow(2, ht)-1

    if num == maxNum:
        return None
    temp = num
    while(1):
        if(temp == maxNum):
            return 1
        elif(temp > maxNum):
            return 0

        temp = temp*2 + 1

print(leftOrRight(4,3))




#
# def leftChildLevel(nums, n, curLevel):
#
#     if(len(nums) == 0):
#         return None, None
#
#     parent = nums[-1]
#     if(parent == n):
#         return curLevel, None
#
#     nextLevel = curLevel-1
#     remaining = nums[:-1]
#     mp = len(remaining)//2
#     half1 = remaining[:mp]
#     half2 = remaining[mp:]
#     lvl1, p1 = leftChildLevel(half1, n, nextLevel)
#     lvl2, p2 = leftChildLevel(half2, n, nextLevel)
#
#     if lvl1 is not None and p1 is not None:
#         return lvl1, p1
#     elif lvl2 is not None and p2 is not None:
#         return lvl2, p2
#     elif lvl1 is not None:
#         return lvl1, parent
#     elif lvl2 is not None:
#         return lvl2, parent
#
#     return None, None
#
#
# nums = []
# h = 10
# print(answer(nums, h))
#
# a = [5]
# b = a[:-1]
# print(b)