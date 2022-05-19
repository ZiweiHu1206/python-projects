
#The program simulates a virtual currency exchange machine on the planet Orion IX.
#The program is to convert between the local curreny (dollars) to COMP202COIN.
#Ziwei Hu 

#Assign default values to variables
SUN1_SET = False
SUN2_SET = True
SOLAR_OBSERVATION_FEE_MULTIPLIER = 0.05
COMP202COIN_FLAT_FEE = 10
COMP202COIN_DOLLAR_EXCHANGE_RATE = 0.05
DOLLAR_COMP202COIN_EXCHANGE_RATE = 0.01
COMP202COIN_SUPPLY = '64'


def display_welcome_menu():
    """ ( ) -> NoneType
    Displays a welcome message and a list with options to the user
    >>> display_welcome_menu()
    Welcome to the Orion IX COMP202COIN virtual exchange machine.
    Available options:
    1. Convert dollars into COMP202COIN
    2. Convert COMP202COIN into dollars
    3. Exit program
    """
    print("Welcome to the Orion IX COMP202COIN virtual exchange machine.")
    print("Available options:")
    print("1. Convert dollars into COMP202COIN")
    print("2. Convert COMP202COIN into dollars")
    print("3. Exit program")
    
    
def get_solar_observation_fee(amount_of_comp202coin):
    """ (str) -> num
    Return the value of solar observation fee by amount of comp202coin, and if both suns set or not
    >>> get_solar_observation_fee("4D2")
    0
    >>> get_solar_observation_fee("A3")
    0
    >>> get_solar-observation_fee("1D")
    0
    """
    #If both suns have set, multiply the given number fo COMP202COINs by SOLAR_OBSERVATION_FEE_MULTIPLIER
    #If still one sun in the sky, the fee will be 0
    if SUN1_SET and SUN2_SET:
        return amount_of_comp202coin * SOLAR_OBSERVATION_FEE_MULTIPLIER
    else:
        return 0
    
    
def get_flat_fee():
    """ ( ) -> int
    Returns the value of COMP202COIN_FLAT_FEE
    >>> get_flat_fee():
    10
    """
    return COMP202COIN_FLAT_FEE


def convert_COMP202COIN_to_dollars(amount_of_comp202coin):
    """ (str) -> float
    Returns the amount of dollars by converting amount_of_comp202coin
    >>> convert_COMP202COIN_to_dollars("A3")
    -1.85
    >>> convert_COMP202COIN_to_dollars("4D3")
    51.75
    >>> convert_COMP202COIN_to_dollars("0")
    -10.0
    """
    #x is Amount of COMP202COINS in base 10 multiply by COMP202-Dollar exchange rate
    #y is Solar observation fee multiply by Amount of COMP202COINs in base 10
    #z is Flat fee
    #Amounts of dollars = variable x minus y minus z, round to 2 decimal places
    x = int(amount_of_comp202coin,16) * COMP202COIN_DOLLAR_EXCHANGE_RATE
    y = get_solar_observation_fee(amount_of_comp202coin) * int(amount_of_comp202coin,16)
    z = get_flat_fee()
    amount_of_dollars = round(float(x - y - z), 2)
    return amount_of_dollars


def convert_dollar_to_COMP202COIN(amount_of_dollars):
    """ (str) -> str
    Returns the amount of COMP202COINs by converting amount_of_dollars
    >>> convert_dollar_to_COMP202COIN("500")
    '0x5'
    >>> convert_dollar_to_COMP202COIN("0")
    '0x0'
    >>> convert_dollar_to_COMP202COIN("12345")
    '0x7b'
    """
    #Amount of COMP202COINs in base 10 = Amount of dollars*Dollar-COMP202COIN exchange rate
    #Round down to the nearest integer
    #Convert COMP202COIN into a base 16 number
    comp202coin_base_10 = float(amount_of_dollars) * DOLLAR_COMP202COIN_EXCHANGE_RATE
    comp202coin_base_10 = int(comp202coin_base_10) 
    comp202coin_base_16 = hex(comp202coin_base_10) 
    return comp202coin_base_16
    
    
def get_excess_dollars_after_conversion(amount_of_dollars):
    """ (float) -> float
    Returns the the amount of excess dollars left over after conversion
    >>> get_excess_dollars_after_conversion(123)
    23
    >>> get_excess_dollars_after_conversion(1001)
    1
    >>> get_excess_dollars_after_conversion(10001)
    1
    """
    #excess dollars is the amount left over after convert to COMP202COIN
    #exchange rate is 0.01, 1 COMP202COIN needs 100 dollars to convert
    excess_dollars = round(amount_of_dollars % 100, 2)
    return excess_dollars


def operate_machine():
    """ ( ) -> NoneType
    Simulates a virtual currency exchange machine
    >>> operate_machine()
    Welcome to the Orion IX COMP202COIN virtual exchange machine.
    Available options:
    1. Convert dollars into COMP202COIN
    2. Convert COMP202COIN into dollars
    3. Exit program
    2
    Enter the amount of COMP202COIN to convert: 4D3
    You have deposited 4D3 COMP202COIN. You will receive 51.75 dollars.
    >>> operate_machine()
    Welcome to the Orion IX COMP202COIN virtual exchange machine.
    Available options:
    1. Convert dollars into COMP202COIN
    2. Convert COMP202COIN into dollars
    3. Exit program
    3
    >>> operate_machine()
    Welcome to the Orion IX COMP202COIN virtual exchange machine.
    Available options:
    1. Convert dollars into COMP202COIN
    2. Convert COMP202COIN into dollars
    3. Exit program
    1
    Enter the amount of dollars to convert: 2456
    You have deposited 2456.0 dollars. You will receive 0x18 COMP202COIN,
    and 56.0 dollars will be returned to you.
    >>> operate_machine()
    Welcome to the Orion IX COMP202COIN virtual exchange machine.
    Available options:
    1. Convert dollars into COMP202COIN
    2. Convert COMP202COIN into dollars
    3. Exit program
    1
    Enter the amount of dollars to convert: 12345
    Your transaction cannot be completed due to insufficient funds.
    """
    #Displays welcome menu and retrives the choice from user
    display_welcome_menu()
    option = int(input()) 
    
    #Execute different block of code according to user's option
    if option == 3:
        return

    elif option == 1:
        money_input = float(input("Enter the amount of dollars to convert: "))
        stock_dollars = int(COMP202COIN_SUPPLY,16) * 100 #Dollars in stock by converting from COMP202COINs in stock
        #If money input(in dollars) by user is larger than dollars in stock, displays this message
        if money_input > stock_dollars:
            print("Your transaction cannot be completed due to insufficient funds.")
        #If money input is not negative and enough supply in stock, execute:
        elif money_input >= 0:
            print("You have deposited", round(money_input,2), "dollars. You will receive", convert_dollar_to_COMP202COIN(str(money_input)), "COMP202COIN,")
            print("and", get_excess_dollars_after_conversion(money_input), "dollars will be returned to you.")
            
    elif option == 2:
        money_input = input("Enter the amount of COMP202COIN to convert: ")
        #Convert money input from string to int type in base 10, if it is not negative, execute:
        if int(money_input,16) >= 0:
            print("You have deposited", money_input, "COMP202COIN. You will receive",convert_COMP202COIN_to_dollars(money_input),"dollars.")
        
            
