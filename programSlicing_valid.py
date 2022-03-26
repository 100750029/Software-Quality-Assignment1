def valid(user_guess, valid_characters, guess_size):
    
    '''
    Returns True if all the characters in user_guess (list) are in
    valid_characters (str) and the length of user_guess is equal
    to guess_size (int).
    
    >>> valid(['H', 'E', 'L', 'L', 'O'], "HELOYT", 5)
    True
    >>> valid(['S'], "S", 3)
    False
    >>> valid(['G', 'R', 'R', 'Y'], "GRBYOP", 4)
    True
    '''
    
    #Checks if the length of user_guess is equal to guess_size
    if len(user_guess) == guess_size:
        #Goes through each character in user_guess
        for character in user_guess:
            #Returns False if the character is not found in valid_characters 
            if character not in valid_characters:
                return False
    else:
        return False
        
    return True

if __name__ == '__main__':

    #Asks the user which level of difficulty they would like to play 
    game_mode = input("What level of difficulty would you like to play (Easy, Regular, Hard): ")
    #Continously re-asks the user for a game_mode as long as game_mode is not valid
    while game_mode != "Easy" and game_mode != "Hard" and game_mode != "Regular":
        #Updates game_mode with the users new game mode 
        game_mode = input("Please enter a valid option (Easy, Regular, Hard): ")

    #Checks which game mode the user picked 
    if game_mode == "Regular":
        # the number of pegs in the answer for the game mode "Regular"
        SIZE = 4
        # the number of guesses the user gets for the game mode "Regular"
        TRIES = 10
    elif game_mode == "Easy":
        # the number of pegs in the answer for the game mode "Easy"
        SIZE = 3
        # the number of guesses the user gets for the game mode "Easy"
        TRIES = 12
    else:
        # the number of pegs in the answer for the game mode "Hard"
        SIZE = 5
        # the number of guesses the user gets for the game mode "Hard"
        TRIES = 8

    # the letters allowed representing the colours
    # green, red, blue, yellow, orange, purple
    VALID_CHARS = 'WORDLE'
  
    #Runs as many times as the users number of tries 
    for i in range(TRIES):
        #Asks the user for their guess 
        guess = input("Please enter guess number " + str(i + 1) + " of length " + str(SIZE) + " using the letters " + VALID_CHARS + ": ")
        #Converts the users guess into a list so that it can be compared to secret_code 
        guess = list(guess)
        #Continously asks the user for a valid guess as long as their guess is not valid
        while not valid(guess, VALID_CHARS, SIZE):
            #Updates guess to store the users new guess 
            guess = input("Please re-enter a valid guess of length " + str(SIZE) + " using the letters " + VALID_CHARS + ": ")
            #Converts the users guess into a list so that it can be compared to secret_code 
            guess = list(guess)
            #Checks if the users guess matches the code (if they have won)
        
    

