# Problem 3 - Printing Out all Available Letters

#Example Usage:
'''
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
'''






def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    # FILL IN YOUR CODE HERE...
    lettersGuessedSet = set(lettersGuessed)
    y = set(string.ascii_lowercase)
    availabeLetters = sorted(y.difference(lettersGuessedSet))
    return ''.join(availabeLetters)
