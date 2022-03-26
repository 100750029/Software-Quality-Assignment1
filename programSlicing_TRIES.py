if __name__ == '__main__':

    #Asks the user which level of difficulty they would like to play 
    game_mode = input("What level of difficulty would you like to play (Easy, Regular, Hard): ")
    #Continously re-asks the user for a game_mode as long as game_mode is not valid
    while game_mode != "Easy" and game_mode != "Hard" and game_mode != "Regular":
        #Updates game_mode with the users new game mode 
        game_mode = input("Please enter a valid option (Easy, Regular, Hard): ")

    #Checks which game mode the user picked 
    if game_mode == "Regular":
        # the number of guesses the user gets for the game mode "Regular"
        TRIES = 10
    elif game_mode == "Easy":
        # the number of guesses the user gets for the game mode "Easy"
        TRIES = 12
    else:
        # the number of guesses the user gets for the game mode "Hard"
        TRIES = 8
        
    # the letters allowed representing the colours
    # green, red, blue, yellow, orange, purple
    VALID_CHARS = 'WORDLE'

    #Creates the secret code using the function create_code() 
    secret_code = VALID_CHARS

    #Runs as many times as the users number of tries 
    for i in range(TRIES):
        #Asks the user for their guess 
        guess = input("Please enter guess number " + str(i + 1)  + " using the letters " + VALID_CHARS + ": ")
        #Converts the users guess into a list so that it can be compared to secret_code 
        guess = list(guess)
        if guess == secret_code:
            print ("Congratualtions! It took you " + str(i + 1) + " guesses to find the code.")
            #Breaks the for loop so that the user is not asked to guess again (the game has ended)
            break
      
    #The secret_code will be given if the user looses because they have no tries left 
    #(the for loop finished and the user was unable to guess the right code)    
    if guess != secret_code:
        print("I'm sorry you lose. The correct code was " + ("").join(secret_code) + ".")
    
    

