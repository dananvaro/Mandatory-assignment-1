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
    
        self.balance *= (1 + self.interest_rate) 

class CheckingAccount(BankAccount):

    transaction_fee = 1

    def withdraw(self, amount):

        InputChecker.numberChecker(amount)

        total = amount+ self.transaction_fee
        
        if not InputChecker.balanceChecker(total,self.balance):
            return

        self.balance -= total


# A main to for better structure
if __name__ == "__main__":

    ## Test cases checking the value and type errors

    # A list with testcases
    testCases = [

        ("Danan",2000), # Successful input
        (2, 2000), # Invalid input due to number "2" in String in input
        ("1",2000), # Invalid input due to number wrapped in String in input
        ("Danan", -2000), # Invalid input  due to a negative input 
        ("Danan", "hdfhdfj"), # Invalid input due to String in integer/float input
        ("Danan", 0) # Invalid input due 0
    ]
    
    # A loop that loops through the test cases
    for name, balance in testCases:

        # A try and except so program won't stop at a ValueError or TypeError
        try: 

            account = BankAccount(name, balance)

            # Prints the successful object created
            print(f"{account.account_info()} has been created.")

        except (ValueError, TypeError) as e:

            # Prints error message 
            print(f"Account has not been created due to error: {e}")

        finally:

            print("Test for error has been completed!")

    # Checks for Class BankAccount
    a1 = BankAccount("Sander Stenvold", 2000)

    print(a1.account_info())

    a1.deposit(60)

    print(a1.account_info())

    a1.withdraw(3000)

    print(a1.account_info())

    # Withdraws more than balance and will give a print back without updating balance
    a1.withdraw(1000)

    print(a1.account_info())

    # Checks for Class SavingsAccount
    a2 = SavingsAccount("Adrian Nilsen", 2000)

    # Inherits account info, deposit and withdrawel from BankAccount
    print(a2.account_info())

    a2.deposit(500)
    
    print(a2.account_info())

    a2.withdraw(20000)

    print(a2.account_info())

    a2.apply_interest()

    print(a2.account_info())

    # Checks for Class SavingsAccount
    a3 = CheckingAccount("Jostein Stegane", 5000) 

    print(a3.account_info())

    a3.deposit(500)

    print(a3.account_info())

    a3.withdraw(3000)

    print(a3.account_info())

    # Checks if you can withdraw with a transaction fee
    a3.withdraw(2499)

    print(a3.account_info())