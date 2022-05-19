#This program generate a palindromic integer from any given number input by the user.
#Print Lynchel numbers at the end of the program.
#Ziwei Hu

def is_integer(user_input):
    """ (str) -> bool
    Returns True if user_input is a positive integer,otherwise displays Error message.
    >>> is_integer('33')
    True
    >>> is_integer('racecar')
    False
    >>> is_integer('-1')
    False
    >>> is_integer('2.22')
    False
    """
    #check whether user's input is a integer
    for char in user_input:
        if char not in "0123456789":
            return False
        
    #check whether the integer is positive
    if int(user_input) < 0:
        return False
    
    return True
    


def generate_palindrome(num):
    """ (str) -> int
    Returns num if num is a palindrome, otherwise add num to its reverse.
    The sum is a new number, returns if it is a palindrome.
    Otherwise continue adding the sum to its reverse, until reaching palindrome.
    >>> generate_palindrome('24')
    66
    >>> generate_palindrome('37')
    121
    >>> generate_palindrome('87')
    4884
    """
    #while num is not palindrome, iterate the following code.
    while str(num) != str(num)[ : :-1]:
        num = int(num) + int( str(num)[ : :-1] )
        
    #num is palindrome, returns num    
    return int(num)



def get_input_num():
    """ (NoneType) -> NoneType
    Retrives input from the user and generate a palindrome.
    >>> get_input_num()
    Please enter a positive integer: 1234
    5555
    >>> get_input_num()
    Please enter a positive integer: 0
    0
    >>> get_input_num()
    Please enter a positive integer: cat
    Error: Please enter a positive integer. 
    """
    
    user_input = input("Please enter a positive integer: ")
    
    #if user_input is a positive integer, generate a palindrome.
    if is_integer(user_input):
        print( generate_palindrome(user_input) )
    else:
        print(input("Error: Please enter a positive integer."))



def lynchel_number():
    """ (NoneType) -> NoneType
    Prints numbers that cannot form a palindrome within 5000 iterations.
    >>> lynchel_number()
    196 295 394 493 
    """
    num = 1
    
    #iterate the number from 1 to 500
    while num <= 500:
        
        test_num = num
        iteration = 0
        #if the number is not a palindrome
        while str(test_num) != str(test_num)[ : :-1]:
            test_num = int(test_num) + int( str(test_num)[ : :-1] )
            
            iteration += 1
            
            #print num if palindrome cannot be generated within 5000 iteration
            if iteration > 5000:
                print(num, end = " ")
                break 
               
        num += 1
    
    
    
        
    
    
    
    
    
    
    

