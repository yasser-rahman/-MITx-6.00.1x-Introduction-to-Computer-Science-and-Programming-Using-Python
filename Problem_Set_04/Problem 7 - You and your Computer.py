def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    
    # TO DO...
    while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            while True:
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif play_mode == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')            
        elif user_input == 'r':
            try:
                hand
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif play_mode == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print('Invalid command.')
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        else:
            print('Invalid command.')
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
 
    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.
 
    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.
 
    4) After the computer or user has played the hand, repeat from step 1
 
    wordList: list (string)
    """
    # TO DO...
    while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            while True:
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif play_mode == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')            
        elif user_input == 'r':
            try:
                hand
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif play_mode == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print('Invalid command.')
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        else:
            print('Invalid command.')

