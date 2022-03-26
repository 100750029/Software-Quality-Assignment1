import time
import datetime

def elapsed_time(func):
    
    def inside_fuection(*args):
        
        start_time = time.time()
        print(func.__name__, 'start time:', datetime.datetime.utcfromtimestamp(start_time))
        valid_function = func(*args)
        end_time = time.time()
        print(func.__name__, 'end time:', datetime.datetime.utcfromtimestamp(end_time))
        time_elapsed = datetime.datetime.utcfromtimestamp(end_time-start_time)
        print(func.__name__, 'Elapsed time:', time_elapsed.strftime('%H:%M:%S.%f'))
        return valid_function
        
    return inside_fuection

@elapsed_time
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

valid_function = valid(['h','h','l','l','h'], ['h','e','l','l','o'], 5)
print("The valid function will output: " + str(valid_function))

