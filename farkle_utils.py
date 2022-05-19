
#This module of program contains Farkle utility functions used to play the game
#Ziwei Hu 
import random

def single_dice_roll():
    """ (NoneType) -> int
    Returns a random integer beween 1 and 6 inclusively,
    Simulates the roll of one 6-side dice.
    >>> random.seed(1229)
    >>> single_dice_roll()
    2
    >>> single_dice_roll()
    4
    >>> single_dice_roll()
    5
    """
    #generate a random integer between 1 and 6 inclusively
    rand_int = random.randint(1,6)
    return rand_int



def dice_rolls(n):
    """ (int) -> list
    Returns a list containing the numbers representing n independent 6-sided dice roll.
    >>> random.seed(1229)
    >>> dice_rolls(6)
    [2, 4, 5, 6, 1, 3]
    >>> dice_rolls(4)
    [3, 2, 2, 3]
    >>> random.seed(1206)
    >>> dice_rolls(6)
    [3, 4, 3, 3, 1, 5]
    >>> dice_rolls(-1)
    Traceback (most recent call last)
    ValueError: The number input should be a positive integer.
    """
    #raise ValueError if n is not positive
    if n <= 0:
        raise ValueError("The number input should be a positive integer.")
    
    #generate a 6-sided dice roll for n times, add to the list
    dice_list = []
    for i in range(n):
        dice_list.append(single_dice_roll())
        
    return dice_list



def contains_repetitions(a_list, n, m):
    """ (list,int,int) -> bool
    Returns True if n appears in a_list at least m times, False otherwise.
    >>> contains_repetitions([1,2,1], 1, 2)
    True
    >>> contains_repetitions([1,2,1,1], 2, 2)
    False
    >>> contains_repetitions([2,2,2,6,2,1], 2, 3)
    True
    >>> contains_repetitions([1,2,3,4,5,6], 1, 0)
    Traceback (most recent call last)
    ValueError: The second integer input should be positive.
    """
    #raise ValueError if m is not a positive integer
    if m <= 0:
        raise ValueError("The second integer input should be positive.")
    
    #counts the occurences of n in a_list 
    times_appears = a_list.count(n)
    
    #returns False if n doesn't appear at least m times, returns True otherwise
    if times_appears < m:
        return False
    else:
        return True
    
    

def pick_random_element(a_list):
    """ (list) -> int
    Returns a random element from the list, return None if the list is empty.
    >>> random.seed(1229)
    >>> pick_random_element([1,2,3,4,5,6])
    2
    >>> pick_random_element([12,0,-1,5,12])
    5
    >>> pick_random_element([])
    """
    #return None if a_list is empty
    if len(a_list) == 0:
        return None
        
    #generate a random index number within the length of a_list, get the element
    rand_index = random.randint(0,len(a_list)-1)
    rand_element = a_list[rand_index]
    
    return rand_element
    


def contains_all(a_list):
    """ (list) -> bool
    Returns True if a_list contains all unique consecutive positive integers,
    starting from 1, False otherwise. The elements can be in any order.
    >>> contains_all([1,2,3,4,5,6])
    True
    >>> contains_all([2,3,1,5,6,4])
    True
    >>> contains_all([1,4,5])
    False
    >>> contains_all([1,1,2])
    False
    """
    #rearrange the elements in an increasing order
    a_list.sort()
    
    #check elements in a_list are consecutive integers starting from 1
    #if not a consecutive integer, return False, otherwise return True
    consecutive_int = 1
    for i in range(len(a_list)):
        if a_list[i] != consecutive_int:
            return False
        consecutive_int += 1
        
    return True
    


def count_num_of_pairs(a_list):
    """ (list) -> int
    Returns the number of pairs in the list
    >>> count_num_of_pairs([1,1,3,3])
    2
    >>> count_num_of_pairs([2,4,2,4,2])
    2
    >>> count_num_of_pairs([1,1,1,1,2,1,2])
    3
    """
    #rearrange the elements in an increasing order
    a_list.sort()
    
    #check if each element is the same to the next element, count if the same
    #then skip to the element after the next element
    num_of_pairs = 0
    skip_element = 0
    for i in range(len(a_list)-1):
        if i < skip_element:
            continue
        if a_list[i] == a_list[i+1]:
            num_of_pairs += 1
            skip_element = i + 2
            
    return num_of_pairs



def is_included(list_1,list_2):
    """ (list,list) -> bool
    Returns True if list_2 is a subset of list_1, False otherwise.
    >>> is_included([1,2,3,4,5],[2,3,4])
    True
    >>> is_included([1,3,4,4,5],[1,3,4,4,5])
    True
    >>> is_included([1,3,5],[1,1])
    False
    """
    #create a copy of list_1 to remain list_1 unchanged
    copy_list_1 = list_1[:]
    
    #check each element of list_2 is in the copy of list_1
    #if True, remove the element in the copy of list_1
    for i in range(len(list_2)):
        if list_2[i] in copy_list_1:
            copy_list_1.remove(list_2[i])
        else:
            return False
        
    return True
            
        
    
def get_difference(list_1,list_2):
    """ (list,list) -> list
    Returns a list which, if added to list_2, would result in a list containing the same
    elements as list_1. If list_2 is not a subset of list_1, returns an empty list.
    >>> get_difference([1,2,3,4,5], [2,4])
    [1,3,5]
    >>> get_difference([1,2,1,3], [1,1])
    [2,3]
    >>> get_difference([1,2,3],[2,2])
    []
    >>> get_difference([1,1,3,4,5], [1,4])
    [1, 3, 5]
    """
    #create an empty list
    new_list = []
    
    #if list_2 is not a subset of list_1, return the empty list
    if not is_included(list_1,list_2):
        return new_list
    
    #make new_list the copy of list_1
    #if a element of list_2 is in new_list, remove the element in new_list
    new_list += list_1
    for i in range(len(list_2)):
        if list_2[i] in new_list:
            new_list.remove(list_2[i])
            
    return new_list
        
#This module of program contains Farkle utility functions used to play the game
#Ziwei Hu 260889365
import random
 
def single_dice_roll():
    """ (NoneType) -> int
    Returns a random integer beween 1 and 6 inclusively,
    Simulates the roll of one 6-side dice.
    >>> random.seed(1229)
    >>> single_dice_roll()
    2
    >>> single_dice_roll()
    4
    >>> single_dice_roll()
    5
    """
    #generate a random integer between 1 and 6 inclusively
    rand_int = random.randint(1,6)
    return rand_int
 
 
 
def dice_rolls(n):
    """ (int) -> list
    Returns a list containing the numbers representing n independent 6-sided dice roll.
    >>> random.seed(1229)
    >>> dice_rolls(6)
    [2, 4, 5, 6, 1, 3]
    >>> dice_rolls(4)
    [3, 2, 2, 3]
    >>> random.seed(1206)
    >>> dice_rolls(6)
    [3, 4, 3, 3, 1, 5]
    >>> dice_rolls(-1)
    Traceback (most recent call last)
    ValueError: The number input should be a positive integer.
    """
    #raise ValueError if n is not positive
    if n <= 0:
        raise ValueError("The number input should be a positive integer.")
    
    #generate a 6-sided dice roll for n times, add to the list
    dice_list = []
    for i in range(n):
        dice_list.append(single_dice_roll())
        
    return dice_list
 
 
 
def contains_repetitions(a_list, n, m):
    """ (list,int,int) -> bool
    Returns True if n appears in a_list at least m times, False otherwise.
    >>> contains_repetitions([1,2,1], 1, 2)
    True
    >>> contains_repetitions([1,2,1,1], 2, 2)
    False
    >>> contains_repetitions([2,2,2,6,2,1], 2, 3)
    True
    >>> contains_repetitions([1,2,3,4,5,6], 1, 0)
    Traceback (most recent call last)
    ValueError: The second integer input should be positive.
    """
    #raise ValueError if m is not a positive integer
    if m <= 0:
        raise ValueError("The second integer input should be positive.")
    
    #counts the occurences of n in a_list 
    times_appears = a_list.count(n)
    
    #returns False if n doesn't appear at least m times, returns True otherwise
    if times_appears < m: 
        return False 
    else: 
        return True 
    
    
 
def pick_random_element(a_list):
    """ (list) -> int
    Returns a random element from the list, return None if the list is empty.
    >>> random.seed(1229)
    >>> pick_random_element([1,2,3,4,5,6])
    2
    >>> pick_random_element([12,0,-1,5,12])
    5
    >>> pick_random_element([])
    """
    #return None if a_list is empty
    if len(a_list) == 0:
        return None
        
    #generate a random index number within the length of a_list, get the element
    rand_index = random.randint(0,len(a_list)-1)
    rand_element = a_list[rand_index]
    
    return rand_element
    
 
 
def contains_all(a_list):
    """ (list) -> bool
    Returns True if a_list contains all unique consecutive positive integers,
    starting from 1, False otherwise. The elements can be in any order.
    >>> contains_all([1,2,3,4,5,6])
    True
    >>> contains_all([2,3,1,5,6,4])
    True
    >>> contains_all([1,4,5])
    False
    >>> contains_all([1,1,2])
    False
    """
    #rearrange the elements in an increasing order
    a_list.sort()
    
    #check elements in a_list are consecutive integers starting from 1
    #if not a consecutive integer, return False, otherwise return True
    consecutive_int = 1
    for i in range(len(a_list)):
        if a_list[i] != consecutive_int:
            return False
        consecutive_int += 1
        
    return True
    
 
 
def count_num_of_pairs(a_list):
    """ (list) -> int
    Returns the number of pairs in the list
    >>> count_num_of_pairs([1,1,3,3])
    2
    >>> count_num_of_pairs([2,4,2,4,2])
    2
    >>> count_num_of_pairs([1,1,1,1,2,1,2])
    3
    """
    #rearrange the elements in an increasing order
    a_list.sort()
    
    #check if each element is the same to the next element, count if the same
    #then skip to the element after the next element
    num_of_pairs = 0
    skip_element = 0
    for i in range(len(a_list)-1):
        if i < skip_element:
            continue
        if a_list[i] == a_list[i+1]:
            num_of_pairs += 1
            skip_element = i + 2
            
    return num_of_pairs
 
 
 
def is_included(list_1,list_2):
    """ (list,list) -> bool
    Returns True if list_2 is a subset of list_1, False otherwise.
    >>> is_included([1,2,3,4,5],[2,3,4])
    True
    >>> is_included([1,3,4,4,5],[1,3,4,4,5])
    True
    >>> is_included([1,3,5],[1,1])
    False
    """
    #create a copy of list_1 to remain list_1 unchanged
    copy_list_1 = list_1[:]
    
    #check each element of list_2 is in the copy of list_1
    #if True, remove the element in the copy of list_1
    for i in range(len(list_2)):
        if list_2[i] in copy_list_1:
            copy_list_1.remove(list_2[i])
        else:
            return False
        
    return True
            
        
    
def get_difference(list_1,list_2):
    """ (list,list) -> list
    Returns a list which, if added to list_2, would result in a list containing the same
    elements as list_1. If list_2 is not a subset of list_1, returns an empty list.
    >>> get_difference([1,2,3,4,5], [2,4])
    [1,3,5]
    >>> get_difference([1,2,1,3], [1,1])
    [2,3]
    >>> get_difference([1,2,3],[2,2])
    []
    >>> get_difference([1,1,3,4,5], [1,4])
    [1, 3, 5]
    """
    #create an empty list
    new_list = []
    
    #if list_2 is not a subset of list_1, return the empty list
    if not is_included(list_1,list_2):
        return new_list
    
    #make new_list the copy of list_1
    #if a element of list_2 is in new_list, remove the element in new_list
    new_list += list_1
    for i in range(len(list_2)):
        if list_2[i] in new_list:
            new_list.remove(list_2[i])
            
    return new_list
        
 