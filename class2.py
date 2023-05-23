class BankAccount:
    def __init__(self, autonumber, balance, clientname, typeofaccount, accountstatus=True):
        self.typeofaccount = typeofaccount
        self.clientname = clientname
        self.accountstatus = accountstatus
        self.balance = balance
        self.autonumber = autonumber

    def deposit(self,deposit):
        if self.accountstatus == True:
            print(f"you are depositing {deposit}")
            self.balance = self.balance + deposit

    def withdraw(self, withdraw):
        if self.balance <= 0 and self.accountstatus == False:
            print("you have no balance to withdraw")
        else:
            print(self.balance - withdraw)

    def checkbalance(self):
        print(self.balance)

    def activateaccount(self):
        if self.accountstatus:
            print("your account is already active")
        else:
            print("fist active the account")

    def deactivateaccount(self):
        if self.balance == 0:
            print("deactivated account")


p1 = BankAccount(1010, 0, "Fabio", "current account")

p1.activateaccount()
p1.deposit(40)
p1.checkbalance()
p1.withdraw(20)
p1.deactivateaccount()
