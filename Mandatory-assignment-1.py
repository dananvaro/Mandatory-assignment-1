import InputChecker

class BankAccount:

    def __init__(self, account_holder, balance=0):

        InputChecker.nameChecker(account_holder)
        InputChecker.numberChecker(balance)
        
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        InputChecker.numberChecker(amount)

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
        
        InputChecker.numberChecker(self.balance)
    
        self.balance *= (1 + self.interest_rate) 

class CheckingAccount(BankAccount):

    transaction_fee = 1

    def withdraw(self, amount):

        InputChecker.numberChecker(amount)

        total = amount+ self.transaction_fee
        
        if not InputChecker.balanceChecker(total,self.balance):
            return

        self.balance -= total

if __name__ == "__main__":
    account = CheckingAccount("Danan", 2000)

    print(account.account_info()) 

    account.withdraw(200)

    print(account.account_info())

    account2 = SavingsAccount("Ramtin", 2000)

    print(account2.account_info())

    account2.apply_interest()

    print(account2.account_info())
