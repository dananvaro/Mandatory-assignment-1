import re
import InputChecker

class BankAccount:

    # Default Atrributes

    def __init__(self, account_holder, balance):

        InputChecker.nameChecker(account_holder)
        InputChecker.numberChecker(balance)
        
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):

        InputChecker.balanceChecker(self.balance, amount)

        self.balance -= amount

    def account_info(self):

        info = f"Account name: {self.account_holder}, Account balance: {self.balance}"
        return info


account = BankAccount("!", 2000)

print(account.account_info())

account.deposit(60)

print(account.account_info())

account.withdraw(3000)

print(account.account_info())