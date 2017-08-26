class BankAccount:
    def __init__(self, name, accountnumber, balance):
        self.name = name
        self.accountnumber = accountnumber
        self.accountbalance = balance
        
    def deposit(self):
        Pass
        # Put code here to add money to a bank account
        
    def withdraw(self):
        Pass
        # Put code here to subtract money from a bank account
        
myAccount = BankAccount("Kevin", 123, 100.00)
print(myAccount)