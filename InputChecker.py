import re

## Input checkers

def nameChecker(name):

    '''
    Checks if input is a String and consists of only letters. If input name consists of numbers it will return a TypeError.
    If input name cosists of special characters is will a ValueError.
    '''
    if not isinstance(name,str):
        raise TypeError("Name must be a string!")
    
    pattern_name=r"^[A-Za-zÆØÅæøå ]+$"
        
    if not re.match(pattern_name, name):
        raise ValueError("Name can't consist of special characters!")

def numberChecker(value):   

    '''
    Checks if input value is a number. If input value is negative it will return a ValueError. 
    If input value is not a integer or decimal it will return TypeError. 
    '''

    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number!")
    if value < 0:
        raise ValueError("Value can't be a negative number!")
    
def transactionChecker(transaction):
    '''
    Checks if input value is a bigger than 0 otherwise will raise a ValueError. The method also checks if the input is a number.
    '''
    numberChecker(transaction)

    if (transaction <= 0):
        raise ValueError("Transaction can't be 0 or negative!")

def balanceChecker(withdrawal,balance):
      
    '''
    Checks if input withdrawal is not greater than balance. If input value is greater than the balance it return a message and False otherwise will it return True. 
    The function also calls the numberChecker. 
    '''
    transactionChecker(withdrawal)

    if (withdrawal > balance):
        print("Insufficient funds!")
        return False
    return True