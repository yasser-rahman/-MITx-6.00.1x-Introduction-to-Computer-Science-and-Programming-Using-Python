
# Problem 1 - Is the Word Guessed

# Example Usage:

# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))
# False










def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in (list(secretWord)):
        if letter not in lettersGuessed:
            return False
        else:
            continue
        
    return True
