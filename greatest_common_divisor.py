#This program displays the greatest common divisor between two numbers

def greatest_common_divisor (x,y):
    """ (num,num) -> num
    Returns the greatest common divisor between x and y
    >>> greatest_common_divisor(7,49)
    7
    >>> greatest_common_divisor(122,2)
    2
    >>> greatest_common_divisor(49,14)
    7
    >>> greatest_common_divisor(0,3)
    
    >>> greatest_common_divisor(-3,1)
    
    """
    while ( x != y ):
        if ( x > y ):
            difference = x - y
            x = difference
        elif ( x < y ):
            difference = y - x
            y = difference
    
    return x

def least_common_multiple (x,y):
    """ (num,num) -> num
    Returns the least common multiple between x and y
    >>> least_common_multiple(34,3)
    102
    >>> least_common_multiple(1,4)
    4
    >>> least_common_multiple(0,33)
    
    """
    num = (x * y) // greatest_common_divisor(x,y)
    return num
    
    
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))

result = least_common_multiple(number_1,number_2)
print(result)
    