import time
import datetime
import random


def elapsed_time(func):
    
    def inside_fuection(*args):
        
        start_time = time.time()
        print(func.__name__, 'start time:', datetime.datetime.utcfromtimestamp(start_time))
        create_code_function = func(*args)
        end_time = time.time()
        print(func.__name__, 'end time:', datetime.datetime.utcfromtimestamp(end_time))
        time_elapsed = datetime.datetime.utcfromtimestamp(end_time-start_time)
        print(func.__name__, 'Elapsed time:', time_elapsed.strftime('%H:%M:%S.%f'))
        return create_code_function
        
    return inside_fuection

@elapsed_time
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

create_code_function = create_code(['D', 'A', 'N', 'I', 'Y', 'A', 'L'], 4)
print("The create_code function will output: " + str(create_code_function))


