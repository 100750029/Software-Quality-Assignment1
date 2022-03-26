import time
import datetime

def elapsed_time(func):
    
    def inside_function(*args):
        
        start_time = time.time()
        print(func.__name__, 'start time:', datetime.datetime.utcfromtimestamp(start_time))
        find_fully_correct_function = func(*args)
        end_time = time.time()
        print(func.__name__, 'end time:', datetime.datetime.utcfromtimestamp(end_time))
        time_elapsed = datetime.datetime.utcfromtimestamp(end_time-start_time)
        print(func.__name__, 'Elapsed time:', time_elapsed.strftime('%H:%M:%S.%f'))
        return find_fully_correct_function
        
    return inside_function

@elapsed_time
def find_fully_correct(answer, guess):
    
    '''
    Returns a list containing the letter "b" for each 
    colour in guess (list of strs) that is in the same position as the 
    same colour in answer (list of strs).  
    
    >>> find_fully_correct(['G', 'B', 'R', 'Y'], ['G', 'R', 'R', 'O'])
    ['b', 'b']
    >>> find_fully_correct(['R', 'R', 'O', 'P'], ['P', 'R', 'R', 'O'])
    ['b']
    >>> find_fully_correct(['P', 'G', 'R', 'O', 'Y'], ['Y', 'G', 'O', 'O', 'Y'])
    ['b', 'b', 'b']
    '''
    #Creates a list that will store the "b" clues 
    correct_b = []
    #Goes through each index value in answer 
    for i in range(len(answer)):
        #Checks if the colour at the index i in guess is 
        #the same colour at the index i in answer
        if guess[i] == answer[i]:
            #Adds a "b" to correct_b
            correct_b.append("b")
            
    return correct_b 

find_fully_correct_function = find_fully_correct(['h','e','l','l','o'], ['h','h','h','h','h'])
print("The find_fully_correct function will output: " + str(find_fully_correct_function))



    