class Transaction:
    def __init__(self, type, val):

        if type != "W" and type != "D":
            raise ValueError("Invalid Transaction Type!")

        self.transType = type
        self.value = val


class Person:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def __str__(self):
        return self.firstName + " " + self.lastName



class Account:
    def __init__(self, id, owner, bal):
        self.minValue = 1000
        self.accountID = id
        self.owner = owner
        self.balance = bal

    def __str__(self):
        balanceStr = "%02d"%abs(self.balance)
        if self.balance > 0:
            return self.accountID + ", " + self.owner.__str__() + ", Balance = " + balanceStr
        else:
            return self.accountID + ", " + self.owner.__str__() + ", Balance = (" + balanceStr + ")"

    def applyTransaction(self, trans):
        if trans.transType == "D":
            self.balance = self.balance + trans.value
        else:
            wd_amt = trans.value
            postWd = round(self.balance - wd_amt, 2)
            if(postWd >= 0):
                self.balance = postWd
            else:
                raise ValueError("Insufficient Funds!")

            if self.balance < self.minValue:
                self.balance = round(self.balance - 10, 2)

class Bank:
    def __init__(self):
        self.accounts = dict()

    def createAccount(self, fn, ln, id):
        for ID in self.accounts.keys():
            if ID == id:
                return
        newOwner = Person(fn, ln)
        newAcc = Account(id, newOwner, 500)
        self.accounts[id] = newAcc

    def applyTransaction(self, id, trans):
        if id not in self.accounts.keys():
            return

        acc = self.accounts[id]
        acc.applyTransaction(trans)







# x = Person("a", "b")
# a = Account("123", x, -100)
# print(a)

