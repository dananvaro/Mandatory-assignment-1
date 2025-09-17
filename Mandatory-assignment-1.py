import InputChecker

class BankAccount:

    def __init__(self, account_holder, balance):

        InputChecker.nameChecker(account_holder)
        InputChecker.numberChecker(balance)
        
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        InputChecker.numberChecker(amount)
        
        self.balance+=amount

    def withdraw(self, amount):
        
        InputChecker.balanceChecker(amount,self.balance)

        self.balance -= amount

    def account_info(self):

        info = f"Account name: {self.account_holder}, Account balance: {self.balance}"
        return info




if __name__ == "__main__":
    account = BankAccount("Danan", 2000)

    print(account.account_info())

    account.deposit(60)

    print(account.account_info())

    account.withdraw(1000)

    print(account.account_info())
