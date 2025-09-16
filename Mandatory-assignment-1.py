import re


class BankAccount:

    # Default Atrributes

    def __init__(self, account_holder, balance):
        
        if not isinstance(account_holder,str):
            raise TypeError("Account name cant consist of numbers!")
        
        pattern_name=r"^[A-Za-zÆØÅæøå ]+$"
        
        if not re.match(pattern_name, account_holder):
            raise ValueError("Name cant consist of special characters!")
        
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number!")
            

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        self.balance -= amount

    def account_info(self):

        info = f"Account name: {self.account_holder}, Account balance: {self.balance}"
        return info


account = BankAccount("Danan", 2000)

print(account.account_info())

account.deposit(60)

print(account.account_info())

account.withdraw(40)

print(account.account_info())