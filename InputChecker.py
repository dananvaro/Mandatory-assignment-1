import re
def nameChecker(input):
    
    if not isinstance(input,str):
            raise TypeError("Account name cant consist of numbers!")
    
    pattern_name=r"^[A-Za-zÆØÅæøå ]+$"
        
    if not re.match(pattern_name, input):
            raise ValueError("Name cant consist of special characters!")
    

def numberChecker(input):
       if not isinstance(input, (int, float)):
            raise TypeError("Balance must be a number!")
       
def balanceChecker(input, balance):
      if (input <= balance):
            raise ValueError("Insufficant funds! Possible withdrawel is: {balance}")