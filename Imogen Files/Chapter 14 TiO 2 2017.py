class BankAccount:
    def __init__(self, name, accountno, balance):
        self.name = name
        self.accountno = accountno
        self.balance = balance

    def __str__(self):
        msg = "Account Name: " + self.name \
        + "\nAccount Number: " + str(self.accountno) \
        + "\nAccount Balance: " + str(self.balance)
        return msg

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount

class InterestAccount(BankAccount):
    def addInterest(self, irate):
        self.balance = self.balance + self.balance * irate
