def swap_elements_in_list(a_list,i,j):
    """ (list,int,int) -> NoneType
    Swap the two elements of a_list that are in position i and j.
    >>> swap_elements_in_list([1,2,3,4,5],0,1)
    [2,1,3,4,5]
    >>> swap_elements_in_list([1,2,3,4,5],-1,1)
    [1,5,3,4,2]
    >>> swap_elements_in_list([1,2,3,4,5],0,5)
    Traceback (most recent call last):
    IndexError: The integers should be in the range of the list.
    """
    if i >= len(a_list) or j >= len(a_list) or i < -len(a_list) or j < -len(a_list):
        raise IndexError("The integers should be in the range of the list.")
    new_str = a_list[i]
    a_list[i] = a_list[j]
    a_list[j] = new_str


def move_up_position(a_list):
    """ (list) -> NoneType
    All the elements are moved up by one position.
    >>> move_up_position([1,2,3,4,5])
    [5,1,2,3,4]
    """
    end = a_list[-1]
    a_list[1:] = a_list[:len(a_list)-1]
    a_list[0] = end
    return a_list



def swap(x,y):
    """ (int,int) -> NoneType
    Prints the value of x and y, swap them, print x and y again.
    >>> swap(3,4)
    inside swap: x is:3 y is:4
    inside swap: x is:4 y is:3
    """
    print("inside swap: x:" + str(x), "y is:" + str(y))
    temp_value = x
    x = y
    y = temp_value
    print("inside swap: x:" + str(x), "y is:" + str(y))
        
def counting(num,step):
    """ (int) -> NoneType
    Counts up to num.
    >>> counting(10,1)
    Counting up to 10: 1 2 3 4 5 6 7 8 9 10
    >>> counting(25,3)
    Counting up to 25 with a step size of 3: 1 4 7 10 13 16 19 22 25
    """
    if type(num) != int:
        raise TypeError("The number entered should be a positive integer.")
    if num <= 0:
        raise ValueError("The number entered should be a positive integer.")
    
    print("Counting up to", num, "with a step size of " + str(step) + ":", end = " ")
    count = 1
    for i in range(0,num,step):
        print(count, end = " ")
        count += step
    print()


def replace_all(string, char_1, char_2):
    """ (str,str,str) -> (str)
    >>> replace_all("squirrel", "r", "s")
    'squissel'
    >>> replace_all("squirrel", "t", "a")
    'squirrel'
    >>> replace_all("squirrel", "ta", "av")
    Traceback (most recent call last):
    ValueError: The character entered should contain exactly one character.
    """
    if len(char_1) != 1 or len(char_2) != 1:
        raise ValueError("The character entered should contain exactly one character.")
    new_str = ""
    for element in string:
        if element == char_1:
            new_str += char_2
        else:
            new_str += element 
    return new_str


def sum_numbers(a_list):
    """ (list) -> int
    Returns the sum of the numbers in a_list, which a_list is a list of integers.
    >>> sum_numbers([1,2,4,5])
    12
    >>> sum_numbers([0,0,0,-1])
    -1
    >>> sum_numbers([])
    Traceback (most recent call last)
    TypeError: The list input should contain all integers.
    >>> sum_number('abc')
    Traceback (most recent call last)
    TypeError: The input should be a list.
    >>> sum_number([1,2,3,'3'])
    Traceback (most recent call last)
    TypeError: The list input should contain all integers.
    """
    if type(a_list) != list:
        raise TypeError("The input should be a list.")
    sum_int = 0
    for element in a_list:
        if type(element) != int:
            raise TypeError("The list input should contain all integers.")
        else:
            sum_int += element
    return sum_int
    
    
    
    
    






