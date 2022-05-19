def print_mult_table(n,m):
    """ (int,int) -> NoneType
    Prints out a multiplication table of n rows and m columns.
    >>> print_mult_table(2, 3)
    1 2 3
    2 4 6
    """
    for row in range(1, n+1):
        for column in range(1, m+1):
            print( column * row, end = " ")
        print()
        
        
def print_squared_table(n):
    """ (int) -> NoneType
    Prints an n by n mutiplication table.
    >>> print_squared_table(10)
    1
    2 4
    3 6 9
    4 8 12 16
    """
    for num in range(1, n+1):
        for i in range(1, num+1):
            print( i * num, end = "  ")
        
        print()
    
def what_print():
    for i in range(1, 5):
        j = 0
        while (j < i):
            print('*', end = '')
            j += 1
        print()
    
def mystery(s):
    t = ''
    for i in range(len(s)):
        for c in s:
            t += c
    return t
    
    
    
def is_prime(n):
    """ (int) -> bool
    Returns True if the n is a prime number,False otherwise.
    >>> is_prime(5)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    """
    if n < 2:
        return False
    
    div = 2
    
    while div < n:
        if n % div == 0:
            return False
        div += 1
        
    return True



def list_prime(n):
    """ (int) -> list
    Returns a list containing the first n primes.
    >>> list_prime(2):
    [2, 3]
    >>> list_prime(5):
    [2, 3, 5, 7, 11]
    >>> list_prime(-1):
    Traceback (most recent call last):
    ValueError: Integer greater than 0 expected.
    >>> list_prime('2')
    Traceback (most recent call last):
    TypeError: Integer expected.
    """
    if type(n) != int:
        raise TypeError("Integer expected.")
    if n < 0:
        raise ValueError("Integer greater than 0 expected.")
    
    new_list = []
    prime_num = 0
    test_num = 2
    
    while prime_num < n:
        if is_prime(test_num):       
            new_list.append(test_num)
            test_num += 1
            prime_num += 1
        else:
            test_num += 1
            continue
    
    print(new_list)


def largest_value(a_list):
    """ (list) -> int
    Returns the largest value in the list.
    >>>largest_value([1,2])
    2
    """
    largest = max(a_list)
    return largest
    
    
def largest_int(a_list):
    """ (list) -> int
    Returns the largest value in the list.
    >>>largest_value([1,2])
    2
    """
    largest = a_list[0]
    for element in a_list:
        if element > largest:
            largest = element
    return largest
    

def move_up(a_list):
    """ (list) -> list
    Returns a list that all the elements have been moved up by one position.
    >>> move_up([2,4,6,8,1,2,3])
    [3,2,4,6,8,1,2]
    """

    end = a_list[-1]
    a_list[1:] = a_list[:len(a_list)-1]
    a_list[0] = end
    return a_list

move_up([2,4,6,8,1,2,3])





    
    