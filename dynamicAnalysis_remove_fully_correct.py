import time
import datetime

def elapsed_time(func):
    
    def inside_function(*args):
        
        start_time = time.time()
        print(func.__name__, 'start time:', datetime.datetime.utcfromtimestamp(start_time))
        remove_fully_correct_function = func(*args)
        end_time = time.time()
        print(func.__name__, 'end time:', datetime.datetime.utcfromtimestamp(end_time))
        time_elapsed = datetime.datetime.utcfromtimestamp(end_time-start_time)
        print(func.__name__, 'Elapsed time:', time_elapsed.strftime('%H:%M:%S.%f'))
        return remove_fully_correct_function
        
    return inside_function

@elapsed_time
def remove_fully_correct(list1, list2):
    
    '''
    Returns a list that has all the characters in list1 
    except for those that are in the same position as the 
    same character in list2.
    
    >>> remove_fully_correct(['R', 'R', 'O', 'P'], ['P', 'R', 'R', 'O'])
    ['R', 'O', 'P']
    >>> remove_fully_correct(['A','B','O','D'], ['D','B','A','D'])
    ['A', 'O']
    >>> remove_fully_correct(['B', 'B', 'B'], ['A', 'B', 'B'])
    ['B']
    '''
    #Creates the new list 
    new_list = []
    #Goes through each index value in list1
    for i in range(len(list1)):
        #Checks if the letter at the index i in list1 is 
        #not the same letter at the index i in list 2
        if list1[i] != list2[i]:
            #Adds that letter to new_list 
            new_list.append(list1[i])
            
    return new_list

remove_fully_correct_function = remove_fully_correct(['h','e','l','l','o'], ['h','l','l','h','h'])
print("The remove_fully_correct function will output: " + str(remove_fully_correct_function))

