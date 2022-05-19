#This program informs the user the time until tomorrow's alarm

#Retrive time and day of the week from the user
day_of_week = int(input("Enter the day of the week(0-6): "))
time = int(input("Enter the time of the day(4 digits integers): "))
vacation_day = input("Is tomorrow a vacation day(Y/N): ")

#Define function that returns the ring time
def ring_time (x, z):
    """ (num,str) -> num
    Return the ring time of the next day
    >>> ring_time(0,"N")
    10
    >>> ring_time(1,"N")
    8
    >>> ring_time(0,"Y")
    12
    """
    if x != 5 and x != 6 :
        if z == "N":
            m = 8
        else:
            m = 10
    if x == 5 or x == 6 :
        if z == "N":
            m = 10
        else:
            m = 12
    return m

#Define function that calculate the hours left 
def hours_left (x, y, z):
    """ (num,num,str) -> num
    Returns the hours remain until tomorrow"s alarm from time x
    >>> hours_left(0,0812,N)
    23
    >>> hours_left(1,1912,N)
    12
    >>> hours_left(1,0000,Y)
    34
    """
    hours = y // 100
    mintues = y % 100
    if mintues == 0:
        hours = 24 - hours + ring_time(x,z)
    else:
        hours = 23 - hours + ring_time(x,z)
    return hours

#Define function that calculate the minutes left
def mintues_left(y):
    """ (num) -> num
    Returns the minutes remain until the alarm
    >>> mintues_left(0000)
    0
    >>> mintues_left(1912)
    48
    >>> mintues_left(1229)
    31
    """
    mintues = y % 100
    if mintues != 0:
        return 60 - mintues
    else:
        return 0

print("There are", hours_left(day_of_week,time,vacation_day), "hours and", mintues_left(time),"minutes until tomorrow's alarm.")
    
