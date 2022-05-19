
#The program is a fair pizza calculator.
#The program converts the one large pizza to the number of small pizza by their diameters.
#The program can also convert the price of large pizza to the price of the amount of pizza the user buys by their diameters.
#Ziwei Hu
import math

def display_welcome_menu():
    """ ( ) -> NoneType
    Displays a welcoming message and a list of options
    >>> display_welcome_menu()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    """
    print("Welcome to the COMP202 fair pizza calculator!")
    print("Please chose one of the following modes:")
    print("A. \"Quantity mode\"")
    print("B. \"Quantity mode\"")
    
    
def area_of_pizza(diameter_pizza):
    """ (int) -> float
    Returns the area of pizza by input the diameter of pizza
    >>> area_pizza(8)
    50.26548245743669
    >>> area_pizza(2)
    3.141592653589793
    >>> area_pizza(-1)
    """
    #Radius of pizza equals diameter of pizza divide by 2.
    #Area of pizza equals pi multiply by the power of 2 of diameter of pizza.
    radius_pizza = diameter_pizza / 2 
    area_pizza = math.pi * pow(radius_pizza,2)
    return area_pizza


def get_fair_quantity(diameter_pizza_1,diameter_pizza_2):
    """ (int,int) -> int
    Returns the amount of small pizza at least the same amount as one large pizza
    >>> get_fair_quantity(10, 7)
    3
    >>> get_fair_quantity(12, 29)
    6
    >>> get_fair_quantity(8, 8)
    1
    """
    area_pizza_1 = area_of_pizza(diameter_pizza_1)
    area_pizza_2 = area_of_pizza(diameter_pizza_2)
    #Calculates the amount of smaller pizza as one larger pizza
    #the amount of small pizza at least is the quotient
    #the excess of large pizza is the remainder
    if diameter_pizza_1 >= diameter_pizza_2:
        amount_pizza_2 = area_pizza_1 // area_pizza_2 
        excess_pizza_1 = area_pizza_1 % area_pizza_2 
        if excess_pizza_1 != 0:
            amount_pizza_2 += 1
        return int(amount_pizza_2)
    else:
        amount_pizza_1 = area_pizza_2 // area_pizza_1 
        excess_pizza_2 = area_pizza_2 % area_pizza_1 
        if excess_pizza_2 != 0:
            amount_pizza_1 += 1
        return int(amount_pizza_1)
        

def get_fair_price(diameter_large_pizza,price_large_pizza,diameter_small_pizza,small_pizza_ordered):
    """ (int,float,int,int) -> float
    Returns the value of price for amount of small pizza ordered by the user
    >>> get_fair_price(12, 10.0, 6, 2)
    5.0
    >>> get_fair_price(8, 8.95, 4, 3)
    6.71
    >>> get_fair_price(30, 30.31, 25, 4)
    84.19
    """
    area_large_pizza = area_of_pizza(diameter_large_pizza)
    area_small_pizza = area_of_pizza(diameter_small_pizza)
    #amount of pizza per dollar is the same for small pizza and large pizza
    #amount of pizza per dollar is amount of large pizza divided by its price
    #price per small pizza is amount of pizza divided by amount of pizza per dollar
    amount_per_dollar = area_large_pizza / price_large_pizza
    price_small_pizza = area_small_pizza / amount_per_dollar 
    total_price = price_small_pizza * small_pizza_ordered
    return round(total_price,2)


def run_pizza_calculator():
    """ ( ) -> NoneType
    Simulates a fair pizza calculator
    >>> run_pizza_calculator()
    Welcome to the COMP202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Quantity mode"

    Enter your choice: 2

    This mode is not supported
    >>> run_pizza_calculator()
    Welcome to the COMP202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Quantity mode"

    Enter your choice: A

    You selected "Quantity mode"

    Enter the diameter of the large pizza: 28
    Enter the diameter of the small pizza: 12

    To be fully satisfied you should order 6 small pizzas
    >>> run_pizza_calculator()
    Welcome to the COMP202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Quantity mode"

    Enter your choice: B

    You selected "Price mode"

    Enter the diameter of the large pizza: 12
    Enter the price of the large pizza: 29.0
    Enter the diameter of the small pizza: 6
    Enter the number of small pizzas you'd like to buy: 12

    The fair price to pay for 12 small pizzas is $87.0
    """
    #Displays welcome menu and retrives the choice from user
    display_welcome_menu()
    choice_of_user = input("\nEnter your choice: ")
    
    #Execute different block of code according to user's option
    if choice_of_user == "A":
        print("\nYou selected \"Quantity mode\"")
        diameter_large_pizza = int(input("\nEnter the diameter of the large pizza: "))
        diameter_small_pizza = int(input("Enter the diameter of the small pizza: "))
        print("\nTo be fully satisfied you should order", get_fair_quantity(diameter_large_pizza,diameter_small_pizza), "small pizzas")
        
    elif choice_of_user == "B":
        print("\nYou selected \"Price mode\"")
        diameter_large_pizza = int(input("\nEnter the diameter of the large pizza: "))
        price_large_pizza = float(input("Enter the price of the large pizza: "))
        diameter_small_pizza = int(input("Enter the diameter of the small pizza: "))
        small_pizza_ordered = int(input("Enter the number of small pizzas you'd like to buy: "))
        print("\nThe fair price to pay for", small_pizza_ordered, "small pizzas is","$" + str(get_fair_price(diameter_large_pizza,price_large_pizza,diameter_small_pizza,small_pizza_ordered)))
        
    else:
        print("\nThis mode is not supported")
        
    
        


    
     
    
#The program is a fair pizza calculator.
#The program converts the one large pizza to the number of small pizza by their diameters.
#The program can also convert the price of large pizza to the price of the amount of pizza the user buys by their diameters.
#Ziwei Hu 260889365
import math
 
def display_welcome_menu():
    """ ( ) -> NoneType
    Displays a welcoming message and a list of options
    >>> display_welcome_menu()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    """
    print("Welcome to the COMP202 fair pizza calculator!")
    print("Please chose one of the following modes:")
    print("A. \"Quantity mode\"")
    print("B. \"Quantity mode\"")
    
    
def area_of_pizza(diameter_pizza):
    """ (int) -> float
    Returns the area of pizza by input the diameter of pizza
    >>> area_pizza(8)
    50.26548245743669
    >>> area_pizza(2)
    3.141592653589793
    >>> area_pizza(-1)
    """
    #Radius of pizza equals diameter of pizza divide by 2.
    #Area of pizza equals pi multiply by the power of 2 of diameter of pizza.
    radius_pizza = diameter_pizza / 2 
    area_pizza = math.pi * pow(radius_pizza,2)
    return area_pizza
 
 
def get_fair_quantity(diameter_pizza_1,diameter_pizza_2):
    """ (int,int) -> int
    Returns the amount of small pizza at least the same amount as one large pizza
    >>> get_fair_quantity(10, 7)
    3
    >>> get_fair_quantity(12, 29)
    6
    >>> get_fair_quantity(8, 8)
    1
    """
    area_pizza_1 = area_of_pizza(diameter_pizza_1)
    area_pizza_2 = area_of_pizza(diameter_pizza_2)
    #Calculates the amount of smaller pizza as one larger pizza
    #the amount of small pizza at least is the quotient
    #the excess of large pizza is the remainder
    if diameter_pizza_1 >= diameter_pizza_2:
        amount_pizza_2 = area_pizza_1 // area_pizza_2 
        excess_pizza_1 = area_pizza_1 % area_pizza_2 
        if excess_pizza_1 != 0:
            amount_pizza_2 += 1
        return int(amount_pizza_2)
    else:
        amount_pizza_1 = area_pizza_2 // area_pizza_1 
        excess_pizza_2 = area_pizza_2 % area_pizza_1 
        if excess_pizza_2 != 0:
            amount_pizza_1 += 1
        return int(amount_pizza_1)
        
 
def get_fair_price(diameter_large_pizza,price_large_pizza,diameter_small_pizza,small_pizza_ordered):
    """ (int,float,int,int) -> float
    Returns the value of price for amount of small pizza ordered by the user
    >>> get_fair_price(12, 10.0, 6, 2)
    5.0
    >>> get_fair_price(8, 8.95, 4, 3)
    6.71
    >>> get_fair_price(30, 30.31, 25, 4)
    84.19
    """
    area_large_pizza = area_of_pizza(diameter_large_pizza)
    area_small_pizza = area_of_pizza(diameter_small_pizza)
    #amount of pizza per dollar is the same for small pizza and large pizza
    #amount of pizza per dollar is amount of large pizza divided by its price
    #price per small pizza is amount of pizza divided by amount of pizza per dollar
    amount_per_dollar = area_large_pizza / price_large_pizza
    price_small_pizza = area_small_pizza / amount_per_dollar 
    total_price = price_small_pizza * small_pizza_ordered
    return round(total_price,2)
 
 
def run_pizza_calculator():
    """ ( ) -> NoneType
    Simulates a fair pizza calculator
    >>> run_pizza_calculator()
    Welcome to the COMP202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Quantity mode"
 
    Enter your choice: 2
 
    This mode is not supported
    >>> run_pizza_calculator()
    Welcome to the COMP202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Quantity mode"
 
    Enter your choice: A
 
    You selected "Quantity mode"
 
    Enter the diameter of the large pizza: 28
    Enter the diameter of the small pizza: 12
 
    To be fully satisfied you should order 6 small pizzas
    >>> run_pizza_calculator()
    Welcome to the COMP202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Quantity mode"
 
    Enter your choice: B
 
    You selected "Price mode"
 
    Enter the diameter of the large pizza: 12
    Enter the price of the large pizza: 29.0
    Enter the diameter of the small pizza: 6
    Enter the number of small pizzas you'd like to buy: 12
 
    The fair price to pay for 12 small pizzas is $87.0
    """
    #Displays welcome menu and retrives the choice from user
    display_welcome_menu()
    choice_of_user = input("\nEnter your choice: ")
    
    #Execute different block of code according to user's option
    if choice_of_user == "A":
        print("\nYou selected \"Quantity mode\"")
        diameter_large_pizza = int(input("\nEnter the diameter of the large pizza: "))
        diameter_small_pizza = int(input("Enter the diameter of the small pizza: "))
        print("\nTo be fully satisfied you should order", get_fair_quantity(diameter_large_pizza,diameter_small_pizza), "small pizzas")
        
    elif choice_of_user == "B":
        print("\nYou selected \"Price mode\"")
        diameter_large_pizza = int(input("\nEnter the diameter of the large pizza: "))
        price_large_pizza = float(input("Enter the price of the large pizza: "))
        diameter_small_pizza = int(input("Enter the diameter of the small pizza: "))
        small_pizza_ordered = int(input("Enter the number of small pizzas you'd like to buy: "))
        print("\nThe fair price to pay for", small_pizza_ordered, "small pizzas is","$" + str(get_fair_price(diameter_large_pizza,price_large_pizza,diameter_small_pizza,small_pizza_ordered)))
        
    else:
        print("\nThis mode is not supported")
        
    
        
 
 
    
     
    
