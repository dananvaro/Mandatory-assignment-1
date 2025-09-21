import InputChecker

class BankAccount:

    def __init__(self, account_holder, balance=0):

        # Checks if name and balance is valid
        InputChecker.nameChecker(account_holder)
        InputChecker.numberChecker(balance)
        
        # A init method that gets exucted everytime when the class is initiated
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money into balance
    def deposit(self, amount):

        # Checks the input is valid and not 0 or below
        InputChecker.transactionChecker(amount)

        # Updates balance
        self.balance+=amount

    def withdraw(self, amount):

        # Uses the balance checker function that checks in amount is a number and 
        # is bigger than the balance if amount is a invalid number it will break out of the method and not update balance
        InputChecker.transactionChecker(amount)

        if not InputChecker.balanceChecker(amount,self.balance):
            return

        # Updates balance
        self.balance -= amount

    # Prints the objects name and balance
    def account_info(self):

        info = f"Account name: {self.account_holder}, Account balance: {self.balance}"
        return info

# Inherits methods from Class BankAccount
class SavingsAccount(BankAccount):
    
    interest_rate = 0.02

    # When called applies intrest
    def apply_interest(self):
    
        self.balance *= (1 + self.interest_rate) 

# Inherits methods from Class BankAccount
class CheckingAccount(BankAccount):

    # Fixed transaction fee at 1 dollar
    transaction_fee = 1.0

    def withdraw(self, amount):

        # Calls a function that checks f inputted number is a number and is above 0
        InputChecker.transactionChecker(amount)

        # Combines the fixed fee and the withdrawal amount
        total = amount+ self.transaction_fee

        if not InputChecker.balanceChecker(total,self.balance):
            return

        self.balance -= total


# A main to for better structure
if __name__ == "__main__":

    ## Test cases checking the value and type errors
    print("-------------------------------------------------------------------------")
    # A list with testcases
    testCases = [

        ("Danan",2000), # Successful input
        (2, 2000), # Invalid input due to number "2" in String in input
        ("1",2000), # Invalid input due to number wrapped in String in input
        ("Danan", -2000), # Invalid input  due to a negative input 
        ("Danan", "hdfhdfj") # Invalid input due to String in integer/float input

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

    
    print("-------------------------------------------------------------------------")

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

    print("-------------------------------------------------------------------------")

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

    print("-------------------------------------------------------------------------")

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