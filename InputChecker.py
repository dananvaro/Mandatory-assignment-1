import re

## Input checkers

def nameChecker(name):

    '''
    Checks if input is a String and consists of only letters. If input name consists of numbers it will return a TypeError.
    If input name cosists of special characters is will a ValueError.
    '''
    if not isinstance(name,str):
        raise ValueError("No numbers accepted!")
    
    pattern_name=r"^[A-Za-zÆØÅæøå ]+$"
        
    if not re.match(pattern_name, name):
        raise TypeError("Name can't consist of special charaters!")

def numberChecker(value):   

    '''
    Checks if input value is a number. If input value is negative it will return a ValueError. 
    If input value is not a integer or decimal it will return TypeError. 
    '''

    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number!")
    if value < 0:
        raise ValueError("Value can't be a negative number!")

def balanceChecker(withdrawel,balance):
      
    '''
    Checks if input withdrawel is not greater than balance. If input value is greater than the balance it return a message and False otherwise will it return True. 
    The function also calls the numberChecker. 
    '''
 
    numberChecker(withdrawel)

    if (withdrawel > balance):
        print(f"Insufficant funds!")
        return False
    return True