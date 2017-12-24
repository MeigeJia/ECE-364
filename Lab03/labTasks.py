def getTotal(accounts):

    totals = list()

    for element in accounts:
        [name, transactions] = element.split(":")
        transactions = transactions.strip()
        transactions = transactions.split()
        for i in range(len(transactions)):
            num = transactions[i]
            num = num[1:]
            transactions[i] = float(num)

        totals.append(round(sum(transactions), 2))

    return totals


def getDoublePalindromes():
    results = list()
    for num in range(10, 1000001):
        if(base10palindrome(num) and base2palindrome(num)):
            results.append(num)
    return results


def base10palindrome(num):
    num = str(num)
    forwardList = list()
    for i in range(len(num)):
        forwardList.append(num[i])

    reverseList = forwardList.copy()
    reverseList.reverse()
    reverseNum = "".join(reverseList)
    num = float(num)
    reverseNum = float(reverseNum)

    if(num == reverseNum):
        return 1
    else:
        return 0

def base2palindrome(num):
    num = bin(num)
    num = num[2:]
    forwardList = list()
    for i in range(len(num)):
        forwardList.append(num[i])

    reverseList = forwardList.copy()
    reverseList.reverse()
    reverseNum = "".join(reverseList)
    num = float(num)
    reverseNum = float(reverseNum)

    if(num == reverseNum):
        return 1
    else:
        return 0

#accounts = ["John Smith: $1.00    $2.00   $3.00 $4.01     ", "John Smith: $10.51    $22.49   $12.00 $5.33   $100.00   "]
#results = getTotal(accounts)
#print(results)


#results = getDoublePalindromes()
#print(results)