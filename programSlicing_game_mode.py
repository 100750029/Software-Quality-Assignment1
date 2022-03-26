if __name__ == '__main__':

    #Asks the user which level of difficulty they would like to play 
    game_mode = input("What level of difficulty would you like to play (Easy, Regular, Hard): ")
    #Continously re-asks the user for a game_mode as long as game_mode is not valid
    while game_mode != "Easy" and game_mode != "Hard" and game_mode != "Regular":
        #Updates game_mode with the users new game mode 
        game_mode = input("Please enter a valid option (Easy, Regular, Hard): ")

    #Checks which game mode the user picked 
    if game_mode == "Regular":
        
        print("The game mode is " + game_mode)
        
    elif game_mode == "Easy":
        
        print("The game mode is " + game_mode)
        
    else:
        print("The game mode is " + game_mode)
