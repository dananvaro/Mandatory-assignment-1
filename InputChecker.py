import re

## Input checkers

def nameChecker(name):

    '''
    Checks if input is a String and consists of only letters. If input name consists of numbers it will return a TypeError.
    If input name cosists of special characters is will a ValueError.
    '''
    if not isinstance(name,str):
        raise TypeError("Account name cant consist of numbers!")
    
    pattern_name=r"^[A-Za-zÆØÅæøå ]+$"
        
    if not re.match(pattern_name, name):
        raise ValueError("Name cant consist of special characters!")
    

def numberChecker(value):   

    '''
    Checks if input value is a number. If input value is negative it will return a ValueError. 
    If input value is not a integer or decimal it will return TypeError. 
    '''
    if value < 0:
        raise ValueError("Can't insert negative numbers!")

    if not isinstance(value, (int, float)):
        raise TypeError("Balance must be a number!")
       
def balanceChecker(withdrawel,balance):
      
    '''
    Checks if input withdrawel is not greater than balance. If input value is greater than the balance it return a ValueError. 
    The function also calls the numberChecker. 
    '''
 
    numberChecker(withdrawel)

    if (withdrawel > balance):
        raise ValueError(f"Insufficant funds!")