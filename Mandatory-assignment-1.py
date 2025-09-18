import InputChecker

class BankAccount:

    def __init__(self, account_holder, balance=0):

        if not InputChecker.nameChecker(account_holder):
            return
        if not InputChecker.numberChecker(balance):
            return
        
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        if not InputChecker.numberChecker(amount):
            return

        self.balance+=amount

    def withdraw(self, amount):
        
        if not InputChecker.balanceChecker(amount,self.balance):
            return

        self.balance -= amount

    def account_info(self):

        info = f"Account name: {self.account_holder}, Account balance: {self.balance}"
        return info

class SavingsAccount(BankAccount):
    
    interest_rate = 0.02

    def apply_interest(self):
        
        if not InputChecker.numberChecker(self.balance):
            return

        self.balance *= (1 + self.interest_rate) 

class CheckingAccount(BankAccount):

    transaction_fee = 1

    def withdraw(self, amount):

        total = amount+ self.transaction_fee
        
        if not InputChecker.balanceChecker(total,self.balance):

            return

        self.balance -= total

if __name__ == "__main__":
    account = CheckingAccount(5, 2000)

    print(account.account_info())

    print(account.account_info())

    account.withdraw(2000)

    print(account.account_info())