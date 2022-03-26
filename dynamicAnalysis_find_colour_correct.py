import time
import datetime

def elapsed_time(func):
    
    def inside_fuection(*args):
        
        start_time = time.time()
        print(func.__name__, 'start time:', datetime.datetime.utcfromtimestamp(start_time))
        find_colour_correct_function = func(*args)
        end_time = time.time()
        print(func.__name__, 'end time:', datetime.datetime.utcfromtimestamp(end_time))
        time_elapsed = datetime.datetime.utcfromtimestamp(end_time-start_time)
        print(func.__name__, 'Elapsed time:', time_elapsed.strftime('%H:%M:%S.%f'))
        return find_colour_correct_function
        
    return inside_fuection

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

@elapsed_time
def find_colour_correct(answer, guess):
    
    '''
    Returns a list containing the letter "w" for each 
    character in guess (list of strs) that is also in answer (list of strs) 
    but isn't in the right position. 
    
    >>> find_colour_correct(['Y','P','G','G'],  ['G','P','O','R'])
    ['w']
    >>> find_colour_correct(['O', 'P', 'P', 'R'], ['O', 'R', 'P', 'P'])
    ['w', 'w']
    >>> find_colour_correct(['Y','P','G'],  ['G','G','O'])
    ['w']
    '''
    #Creates the list that will store all the "w" clues 
    correct_w = []
    #Removes all the colours that are in the right position from both answer and guess
    new_guess = remove_fully_correct(guess, answer)
    new_answer = remove_fully_correct(answer, guess)
    #Goes through each colour in new_guess
    for colour in new_guess:
        #Checks if the colour is in new_answer
        if colour in new_answer:
            #Adds a "w" to correct_w
            correct_w.append("w")
            #Removes that colour from new_answer so that it isn't checked twice 
            new_answer.remove(colour)
            
    return correct_w 

find_colour_correct_function = find_colour_correct(['y','p','g'], ['g','g','o'])
print("The find_colour_correct function will output: " + str(find_colour_correct_function))


