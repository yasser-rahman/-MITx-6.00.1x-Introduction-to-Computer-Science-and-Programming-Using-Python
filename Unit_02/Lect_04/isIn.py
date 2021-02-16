def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    val1 = len(aStr)//2
    if aStr == "":
        return False
    elif len(aStr) <=1 and char != aStr[0]:
        return False
    elif char == aStr[val1]:
        return True
    elif char < aStr[val1]:
        val2 = aStr[:val1]
        return isIn(char,val2)
    elif char > aStr[val1]:
        val3 = aStr[val1:]
        return isIn(char, val3)
    elif char != val2 and char != val3:
        return False
