def is_palindrome(s):
    """ (str) -> bool
    Returns True if it is a palindrome, False otherwise.
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("Mom")
    True
    >>> is_palindrome("A nut for a jar of tuna")
    True
    >>> is_palindrome("apple")
    False
    """
    s = s.lower()
    s = s.replace(" ",'')    
    return s == s[ : :-1]


def is_palindrome_2(number):
    """ (str) -> bool
    Returns True if number is a palindrome, False otherwise.
    >>> is_palindrome('12321')
    True
    >>> is_palindrome('123')
    False
    >>> is_palindrome('racecar')
    True
    """
    #check whether the number is a palindrome.
    return number == number[ : :-1]




def remove_duplicates(s):
    """ (str) -> str
    Returns a string containing all unique letters in s.
    >>> remove_duplicates("banana")
    'ban'
    >>> remove_duplicates("background")
    'background'
    """
    no_duplicate = ""
    
    for char in s.lower():
        if char not in no_duplicate:
            no_duplicate = no_duplicate + char 
    return no_duplicate

def count_common_letters(s,t):
    """ (str) -> int
    Returns how many letters the two strings have in common.
    >>> count_common_letters("banana", "cat")
    1
    >>> count_common_letters("Silent", "listen")
    6
    """
    s = s.lower()
    s = remove_duplicates(s)
    t = t.lower()
    t = remove_duplicates(t)
    count = 0
    for char in s:
        if char in t:
            count += 1      
        
    return count
            
    
    
    
    
    
    
    
    
    
    
    
    
    