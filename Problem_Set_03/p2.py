# Problem 2 - Getting the User's Guess

# Example Usage:

# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))
#'_ pp_ e'




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    gessedWordList = ['-' for i in range(len(secretWord))]
    secretWordList = list(secretWord)
    for letter in lettersGuessed:
        if letter in secretWordList:
            for i in range(len(secretWordList)):
                if letter == secretWordList[i]:
                    gessedWordList[i] = secretWordList[i]
                else: 
                    continue
    return ''.join(gessedWordList)
                
