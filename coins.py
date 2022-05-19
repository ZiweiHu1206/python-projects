

#The program provide several functions to manipulate COMP202COIN in base202 and base10
#Ziwei Hu 

#assign global variable to manipulate through the program
BASE8_CHARS = "01234567"
BASE202_CHARS = "0C2OMPIN"


def base10_to_202(amt_in_base10):
    """ (int) -> str
    Convert amt_in_base10 to corresponding amount in base 202.
    >>> base10_to_202(202)
    '0c00000OC2'
    >>> base10_to_202(0)
    '0c00000000'
    >>> base10_to_202(12345678)
    '0cPN0I0PCI'
    >>> base10_to_202(-1)
    Traceback (most recent call last)
    ValueError: The amount should not be a negative integer.
    """
    
    #if the amt entered is a negative integer, raise ValueError
    if amt_in_base10 < 0:
        raise ValueError("The amount should not be a negative integer.")
        
    #convert the amt in base10 to amt in base8
    amt_in_base8 = oct(amt_in_base10)
    
    #iterate through each character of amt in base8 except for the first two characters
    #to convert amt in base8 to amt in base202
    amt_in_base202 = ""
    for i in range(2,len(amt_in_base8)):
        index = BASE8_CHARS.find(amt_in_base8[i])
        amt_in_base202 += BASE202_CHARS[index]
    
    #if amt in base202 doesn't reach full eight characters, add '0' in front of it
    while len(amt_in_base202) < 8:
        amt_in_base202 = "0" + amt_in_base202
    
    #add '0c' in front of amt in base 202
    amt_in_base202 = "0c" + amt_in_base202
     
    return amt_in_base202



def base202_to_10(amt_in_base202):
    """ (str) -> int
    Convert amt_in_base202 to amt in base 10.
    >>> base202_to_10('0c00000OC2')
    202
    >>> base202_to_10('0c00000000')
    0
    >>> base202_to_10('0cPN0I0PCI')
    12345678
    >>> base202_to_10('-0c00000OC2')
    Traceback (most recent call last)
    ValueError: The amount entered should not be negative.
    """
    
    #if the amount input is negative, raise ValueError
    if amt_in_base202[0] == '-':
        raise ValueError("The amount entered should not be negative.")
    
    #iterate through each character of amt in base202 except for the first two characters
    #to convert amt in base202 to amt in base8
    amt_in_base8 = ""
    for i in range(2,10):
        index = BASE202_CHARS.find(amt_in_base202[i])
        amt_in_base8 += BASE8_CHARS[index]
    
    #convert amt in base8 to amt in base 10
    amt_in_base10 = int(amt_in_base8,8)
        
    return amt_in_base10
    
    
    
def is_base202(text):
    """ (str) -> bool
    Returns True if text is a valid 10-character COMP202COIN, False otherwise.
    >>> is_base_202('0cPN0I0PCI')
    True
    >>> is_base_202('acPN0I0PCI')
    False
    >>> is_base_202('00000OC2')
    False
    >>> is_base_202('I like comp202')
    False
    """
    
    #if text doesn't contain exactly 10 characters,or first 2 characters are not'0c',
    #then return False
    if len(text) != 10:
        return False
    elif text[0] != "0":
        return False
    elif text[1] not in "Cc":
        return False
    
    #iterate through each character to check membership of BASE202_CHARS
    for i in range(2,10):
        if text[i] not in BASE202_CHARS:
            return False
        
    return True
    
    

def coins_list(text):
    """ (str) -> list
    Returns a list containing all COMP202COIN in base 200 in text
    >>> coins_list("BANKING TRANSACTIONS....PLANET ORION......FEBURARY /15,3019......
    0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... /FEBRUARY17, 3019.
    .........0C24242412")
    ['0cCCMMPP22', '0cOCOCOCOC']
    >>> coins_list("0C0C0C0C0C0CCCMMPP22")
    ['0C0C0C0C0C', '0C0CCCMMPP']
    >>> coins_list('abcd1234')
    []
    """
    
    #create an empty list, iterate through each 10-character in text to check
    #if the 10-character is COMP202COIN, append to the list, skip to the next 10-character
    coin_list = []
    skip_characters = 0
    for i in range(len(text)):
        if i < skip_characters:
            continue
        if is_base202(text[i:i+10]):
            coin_list.append(text[i:i+10])
            skip_characters = i + 10
            
    return coin_list
    
    
    
def get_nth_base202_amount(text,n):
    """ (str,int) -> str
    Returns the n'th 10-character COMP202COIN in text.
    >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15,
    3019......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... / FEBRUARY
    17, 3019..........0C24242412", 0)
    '0cCCMMPP22'
    >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15, 30
    19.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC........./ FEBRUARY 17,
    3019..........0C24242412", 3)
    ''
    >>> get_nth_base202_amount("0c0cCCMMPP22",0)
    '0cCCMMPP22'
    >>> get_nth_base202_amount("0C0CCCMMPP22",1)
    ''
    >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15,
    3019......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... / FEBRUARY
    17, 3019..........0C24242412", -2)
    Traceback (most recent call last)
    ValueError: n should be a non-nagative integer.
    """
    
    #if n is a negative integer, raise ValueError 
    if n < 0:
        raise ValueError("n should be a non-nagative integer.")
    
    #if there is no n'th element in the list, returns empty string
    #otherwise returns the n'th element of the list
    nth_base202_amt = ''
    if n >= len(coins_list(text)):
        return nth_base202_amt     
    else:
        nth_base202_amt += coins_list(text)[n]
        return nth_base202_amt
    
    

def get_total_dollar_amount(text):
    """ (str) -> int
    Returns the total dollar amount in base 10 of all COMP202COIN present in text.
    >>> get_total_dollar_amount("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15,
    3019......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... / FEBRUARY
    17, 3019..........0C24242412")
    9167275
    >>> get_total_dollar_amount("abcdefg")
    0
    >>> get_total_dollar_amount("0c00000OC2..0cPN0I0PCI.....acPN0I0PCI")
    12345880
    """
    
    #convert every element to amount in base 10, add together
    total_dollar_amount = 0
    for element in coins_list(text):
        total_dollar_amount += base202_to_10(element)
    
    return total_dollar_amount



def reduce_amounts(text, limit):
    """ (str, int) -> str
    Returns the same string if total dollar amount is less than or equal to limit,
    otherwise reduce each amount by percent decrease, returns the updated string
    >>> reduce_amounts('0c000000C2', 5)
    '0c0000000P'
    >>> reduce_amounts('0cCCMMPP22     0cOCOCOCOC', 9000000)
    '0cCCOCMCI0     0cO0NOPNCN'
    >>> reduce_amounts('abcd1234', 1000)
    'abcd1234'
    >>> reduce_amounts("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15,3019......
    0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... / FEBRUARY17,3019....
    ......0C24242412",10000)
    'BANKING TRANSACTIONS....PLANET ORION......FEBURARY/ 15,3019......0c0000P2IC........
    FEBRUARY 16, 3019..........0c000CICOI......... /FEBRUARY17, 3019..........0C24242412'
    """
    
    #raise ValueError if limit is a negative integer
    if limit < 0:
        raise ValueError("The limit should be a non-negative integer")
    
    #if total dollar amount is less than or equal to the limit, return the same string
    if get_total_dollar_amount(text) <= limit:
        return text
    
    #if greater than the limit, calculate the difference and percent decrease
    difference = get_total_dollar_amount(text) - limit
    percent_decrease = difference / get_total_dollar_amount(text) 
    
    #create a new string, iterate through each 10-character in text to check
    new_text = ""
    skip_characters = 0
    for i in range(len(text)):
        if i < skip_characters:
            continue
        
        #if 10-character string is COMP202COIN in base202, updated COMP202COIN
        #then skip to the next 10-character
        if is_base202(text[i:i+10]):
            updated_coins = int(base202_to_10(text[i:i+10]) * (1 - percent_decrease))
            updated_coins = base10_to_202(updated_coins)
            new_text += updated_coins
            skip_characters = i + 10
            
        else:
            new_text += text[i]
    
    return new_text
    
#The program provide several functions to manipulate COMP202COIN in base202 and base10
#Ziwei Hu 260889365
 
#assign global variable to manipulate through the program
BASE8_CHARS = "01234567"
BASE202_CHARS = "0C2OMPIN"
 
 
def base10_to_202(amt_in_base10):
    """ (int) -> str
    Convert amt_in_base10 to corresponding amount in base 202.
    >>> base10_to_202(202)
    '0c00000OC2'
    >>> base10_to_202(0)
    '0c00000000'
    >>> base10_to_202(12345678)
    '0cPN0I0PCI'
    >>> base10_to_202(-1)
    Traceback (most recent call last)
    ValueError: The amount should not be a negative integer.
    """
    
    #if the amt entered is a negative integer, raise ValueError
    if amt_in_base10 < 0:
        raise ValueError("The amount should not be a negative integer.")
        
    #convert the amt in base10 to amt in base8
    amt_in_base8 = oct(amt_in_base10)
    
    #iterate through each character of amt in base8 except for the first two characters
    #to convert amt in base8 to amt in base202
    amt_in_base202 = ""
    for i in range(2,len(amt_in_base8)):
        index = BASE8_CHARS.find(amt_in_base8[i])
        amt_in_base202 += BASE202_CHARS[index]
    
    #if amt in base202 doesn't reach full eight characters, add '0' in front of it
    while len(amt_in_base202) < 8:
        amt_in_base202 = "0" + amt_in_base202
    
    #add '0c' in front of amt in base 202
    amt_in_base202 = "0c" + amt_in_base202
     
    return amt_in_base202
 
 
 
def base202_to_10(amt_in_base202):
    """ (str) -> int
    Convert amt_in_base202 to amt in base 10.
    >>> base202_to_10('0c00000OC2')
    202
    >>> base202_to_10('0c00000000')
    0
    >>> base202_to_10('0cPN0I0PCI')
    12345678
    >>> base202_to_10('-0c00000OC2')
    Traceback (most recent call last)
    ValueError: The amount entered should not be negative.
    """
    
    #if the amount input is negative, raise ValueError
    if amt_in_base202[0] == '-':
        raise ValueError("The amount entered should not be negative.")
    
    #iterate through each character of amt in base202 except for the first two characters
    #to convert amt in base202 to amt in base8
    amt_in_base8 = ""
    for i in range(2,10):
        index = BASE202_CHARS.find(amt_in_base202[i])
        amt_in_base8 += BASE8_CHARS[index]
    
    #convert amt in base8 to amt in base 10
    amt_in_base10 = int(amt_in_base8,8)
        
    return amt_in_base10
    
    
    
def is_base202(text):
    """ (str) -> bool
    Returns True if text is a valid 10-character COMP202COIN, False otherwise.
    >>> is_base_202('0cPN0I0PCI')
    True
    >>> is_base_202('acPN0I0PCI')
    False
    >>> is_base_202('00000OC2')
    False
    >>> is_base_202('I like comp202')
    False
    """
    
    #if text doesn't contain exactly 10 characters,or first 2 characters are not'0c',
    #then return False
    if len(text) != 10: 
        return False 
    elif text[0] != "0": 
        return False 
    elif text[1] not in "Cc": 
        return False 
    
    #iterate through each character to check membership of BASE202_CHARS
    for i in range(2,10):
        if text[i] not in BASE202_CHARS:
            return False
        
    return True
    
    
 
def coins_list(text):
    """ (str) -> list
    Returns a list containing all COMP202COIN in base 200 in text
    >>> coins_list("BANKING TRANSACTIONS....PLANET ORION......FEBURARY /15,3019......
    0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... /FEBRUARY17, 3019.
    .........0C24242412")
    ['0cCCMMPP22', '0cOCOCOCOC']
    >>> coins_list("0C0C0C0C0C0CCCMMPP22")
    ['0C0C0C0C0C', '0C0CCCMMPP']
    >>> coins_list('abcd1234')
    []
    """
    
    #create an empty list, iterate through each 10-character in text to check
    #if the 10-character is COMP202COIN, append to the list, skip to the next 10-character
    coin_list = []
    skip_characters = 0
    for i in range(len(text)):
        if i < skip_characters:
            continue
        if is_base202(text[i:i+10]):
            coin_list.append(text[i:i+10])
            skip_characters = i + 10
            
    return coin_list
    
    
    
def get_nth_base202_amount(text,n):
    """ (str,int) -> str
    Returns the n'th 10-character COMP202COIN in text.
    >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15,
    3019......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... / FEBRUARY
    17, 3019..........0C24242412", 0)
    '0cCCMMPP22'
    >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15, 30
    19.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC........./ FEBRUARY 17,
    3019..........0C24242412", 3)
    ''
    >>> get_nth_base202_amount("0c0cCCMMPP22",0)
    '0cCCMMPP22'
    >>> get_nth_base202_amount("0C0CCCMMPP22",1)
    ''
    >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15,
    3019......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... / FEBRUARY
    17, 3019..........0C24242412", -2)
    Traceback (most recent call last)
    ValueError: n should be a non-nagative integer.
    """
    
    #if n is a negative integer, raise ValueError 
    if n < 0:
        raise ValueError("n should be a non-nagative integer.")
    
    #if there is no n'th element in the list, returns empty string
    #otherwise returns the n'th element of the list
    nth_base202_amt = ''
    if n >= len(coins_list(text)):
        return nth_base202_amt     
    else:
        nth_base202_amt += coins_list(text)[n]
        return nth_base202_amt
    
    
 
def get_total_dollar_amount(text):
    """ (str) -> int
    Returns the total dollar amount in base 10 of all COMP202COIN present in text.
    >>> get_total_dollar_amount("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15,
    3019......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... / FEBRUARY
    17, 3019..........0C24242412")
    9167275
    >>> get_total_dollar_amount("abcdefg")
    0
    >>> get_total_dollar_amount("0c00000OC2..0cPN0I0PCI.....acPN0I0PCI")
    12345880
    """
    
    #convert every element to amount in base 10, add together
    total_dollar_amount = 0
    for element in coins_list(text):
        total_dollar_amount += base202_to_10(element)
    
    return total_dollar_amount
 
 
 
def reduce_amounts(text, limit):
    """ (str, int) -> str
    Returns the same string if total dollar amount is less than or equal to limit,
    otherwise reduce each amount by percent decrease, returns the updated string
    >>> reduce_amounts('0c000000C2', 5)
    '0c0000000P'
    >>> reduce_amounts('0cCCMMPP22     0cOCOCOCOC', 9000000)
    '0cCCOCMCI0     0cO0NOPNCN'
    >>> reduce_amounts('abcd1234', 1000)
    'abcd1234'
    >>> reduce_amounts("BANKING TRANSACTIONS....PLANET ORION......FEBURARY / 15,3019......
    0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC......... / FEBRUARY17,3019....
    ......0C24242412",10000)
    'BANKING TRANSACTIONS....PLANET ORION......FEBURARY/ 15,3019......0c0000P2IC........
    FEBRUARY 16, 3019..........0c000CICOI......... /FEBRUARY17, 3019..........0C24242412'
    """
    
    #raise ValueError if limit is a negative integer
    if limit < 0:
        raise ValueError("The limit should be a non-negative integer")
    
    #if total dollar amount is less than or equal to the limit, return the same string
    if get_total_dollar_amount(text) <= limit:
        return text
    
    #if greater than the limit, calculate the difference and percent decrease
    difference = get_total_dollar_amount(text) - limit
    percent_decrease = difference / get_total_dollar_amount(text) 
    
    #create a new string, iterate through each 10-character in text to check
    new_text = ""
    skip_characters = 0
    for i in range(len(text)):
        if i < skip_characters:
            continue
        
        #if 10-character string is COMP202COIN in base202, updated COMP202COIN
        #then skip to the next 10-character
        if is_base202(text[i:i+10]):
            updated_coins = int(base202_to_10(text[i:i+10]) * (1 - percent_decrease))
            updated_coins = base10_to_202(updated_coins)
            new_text += updated_coins
            skip_characters = i + 10
            
        else:
            new_text += text[i]
    
    return new_text
    
 
