import random

def create_code(characters, length):
    
    '''
    Returns a list the length of length (int) with any 
    random single characters from characters (str).
    
    >>> create_code("Daniyal", 4)
    ['D', 'i', 'y', 'l']
    >>> create_code("Hello", 3)
    ['H', 'H', 'H']
    '''
    
    #Creates the list that will store the code
    code = []
    #Adds a random letter from characters to code length amount of times
    for i in range(length):
        code.append(random.choice(characters))
        
    return code 

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
  
    #Creates the secret code using the function create_code() 
    secret_code = create_code(VALID_CHARS, SIZE)

    #Runs as many times as the users number of tries 
    for i in range(TRIES):
        #Asks the user for their guess 
        guess = input("Please enter guess number " + str(i + 1) + " of length " + str(SIZE) + " using the letters " + VALID_CHARS + ": ")
        #Converts the users guess into a list so that it can be compared to secret_code 
        guess = list(guess)
        #Checks if the users guess matches the code (if they have won)
        if guess == secret_code:
            print ("Congratualtions! It took you " + str(i + 1) + " guesses to find the code.")
            #Breaks the for loop so that the user is not asked to guess again (the game has ended)
            break
      
    #The secret_code will be given if the user looses because they have no tries left 
    #(the for loop finished and the user was unable to guess the right code)    
    if guess != secret_code:
        print("I'm sorry you lose. The correct code was " + ("").join(secret_code) + ".")
    
    
