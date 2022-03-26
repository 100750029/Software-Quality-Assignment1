if __name__ == '__main__':

    # the letters allowed representing the colours
    VALID_CHARS = 'WORDLE'
  
    #Creates the secret code using the function create_code() 
    secret_code = VALID_CHARS
    
    #Asks the user for their guess 
    guess = input("Please enter guess using the letters " + VALID_CHARS + ": ")

    #Checks if the users guess matches the code (if they have won)
    if guess == secret_code:
        print ("Congratulations! you guessed the code.")
        
    else:
        print("I'm sorry you lose. The correct code was " + ("").join(secret_code) + ".")
    
    
