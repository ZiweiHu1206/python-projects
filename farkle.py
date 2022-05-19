#This module of program contains the functions that allow us to execute a game of Farkle,
#between mutiple players.
#Ziwei Hu 260889365
import random
from farkle_utils import *

#assign global variable to manipulate through the program
SINGLE_ONE = 100
SINGLE_FIVE = 50
TRIPLET_MULTIPLIER = 100
STRAIGHT = 3000
THREE_PAIRS = 1500


def compute_score(a_list):
    """ (list) -> int
    Returns the highest points scored of a_list, each element represents a 6-sided dice
    >>> compute_score([1,1,1])
    1000
    >>> compute_score([1,1,2,2,4,4])
    1500
    >>> compute_score([1,2,3,4,5,6])
    3000
    >>> compute_score([5,1,5,5])
    600
    >>> compute_score([1,1,3])
    0
    >>> compute_score([1,1,1,1,1,1])
    2000
    >>> compute_score([5,5,5,5,5,5])
    1500
    >>> compute_score([2,-1,2])
    Traceback (most recent call last)
    ValueError: The list should contain integers between 1 and 6.
    """
    #raise ValueError if the element is not integer between 1 and 6
    for element in a_list:
        if element < 1 or element > 6:
            raise ValueError("The list should contain integers between 1 and 6.")
        
    #create a variable score to add on
    score = 0
    
    #if a_list is 1 to 6, add STRAIGHT to score
    if contains_all(a_list) and len(a_list) == 6:
        score += STRAIGHT
        a_list = []
        
    #if a_list contains 3 pairs, and not all the elements equal to 1, add THREE_PAIRS
    #if all the elements equal to 1, mutiply the TRIPLET_MULTIPLIER by 20
    if count_num_of_pairs(a_list) == 3:
        if a_list == [1,1,1,1,1,1]:
            score += TRIPLET_MULTIPLIER * 20
            a_list = []
        else:
            score += THREE_PAIRS
            a_list = []
    
    #if there is three 1's in a_list, add score by mutipling the TRIPLET_MULTIPLIER by 10
    if contains_repetitions(a_list, 1, 3):
        score += TRIPLET_MULTIPLIER * 10
        a_list = get_difference(a_list,[1,1,1])
    
    #check if there is triplet from 2 to 6, if so, add score
    for i in range(2,7):
        if contains_repetitions(a_list, i, 3):
            score += TRIPLET_MULTIPLIER * i
            a_list = get_difference(a_list,[i,i,i])
         
    #while there is 1 in a_list, add score     
    while 1 in a_list:
        score += SINGLE_ONE
        a_list.remove(1)
    
    #while there is 5 in a_list, add score
    while 5 in a_list:
        score += SINGLE_FIVE
        a_list.remove(5)
    
    #if not all elements can be used to score, the total score is 0
    if len(a_list) > 0:
        score = 0
    
    return score




def get_winners(a_list, score_to_win):
    """ (list,int) -> list
    Returns a list of players with the highest score in a_list,
    which reached or surpassed score_to_win.
    >>> get_winners([500,1000,50],5000)
    []
    >>> get_winners([5000,10000,200],10000)
    [2]
    >>> get_winners([50,50,10,5],5)
    [1,2]
    >>> get_winners([50,-50,1],5)
    Traceback (most recent call last)
    ValueError: The list should contain all positive integers.
    >>> get_winners([1,2,3,4],-2)
    Traceback (most recent call last)
    ValueError: The winning score should be a positive integer.
    """
    #raise ValueError if there is non-positive integer in a_list
    for element in a_list:
        if element <= 0:
            raise ValueError("The list should contain all positive integers.")
        
    #raise ValueError if score_to_win is not positive
    if score_to_win <= 0:
        raise ValueError("The winning score should be a positive integer.")
    
    #create an empty list to add winner, get the maximum value in a_list
    winner_list = []
    highest_score = max(a_list)
    
    #if the highest score is lower than the score to win, returns empty string
    if highest_score < score_to_win:
        return winner_list
    
    #if there is any element equals to highest_score, appends its position to winner_list
    for i in range(len(a_list)):
        if a_list[i]                                                                                                               == highest_score:
            winner_list.append(i+1)
            
    return winner_list
            
            
        
        
def play_one_turn(player):
    """ (int) -> int
    Returns the score of player after they play this turn.
    """
    #raise ValueError if the number representing the play is non-positive
    if player <= 0:
        raise ValueError("The number of player should be a positive integer.")
    
    print("Player", player, "it's your turn!")
    print()
    
    #set the initial total score to 0, and the player starts with 6 dice
    total_score = 0
    dice_list = dice_rolls(6)
        
        
        
    #asks the user whether they would like to roll or pass
    #if the user still has dice remains
    while len(dice_list) != 0:
        
        user_decision = input("What would you like to do? (roll/pass): ")
        user_decision = user_decision.lower()
        
        #if the user chose not to roll, return the score
        if user_decision != "roll":
            print()
            return total_score
        
        
        #roll all the dice remaining again
        dice_list = dice_rolls(len(dice_list))
        
        #print the result of dice
        print("Here's the result of rolling your", len(dice_list),"dice:", end = " ")
        for i in range(len(dice_list)):
            dice_list[i] = str(dice_list[i])
        print(', '.join(dice_list))
        
        
        #asks the player to select the scoring dice to set aside
        user_selected = input("Please select the dice to set aside for scoring: ")
        scoring_dice = user_selected.split()
        
        #while the player selects dice that have not been rolled, asks again
        while not is_included(dice_list,scoring_dice):
            user_selected = input("You do not have these dice. Select again: ")
            scoring_dice = user_selected.split()
        
        #change all elements in lists to integer 
        for i in range(len(scoring_dice)):
            scoring_dice[i] = int(scoring_dice[i])
        
        for i in range(len(dice_list)):
            dice_list[i] = int(dice_list[i])
    
        #remove the asided scoring dice from original dice list
        dice_list = get_difference(dice_list, scoring_dice)

        
        #computes the current score and the remaining dice
        #if "farkled", all the points for this turn are lost
        score = compute_score(scoring_dice)
        if score == 0:
            total_score = 0
            dice_list += scoring_dice
            print("Farkle! All the points accumulated up to now are lost.")
        else:
            total_score += score
            
        #if there is no remaining dice, the player may continue their turn with new 6 dice
        if len(dice_list) == 0:
            print("HOT DICE! You are on a roll. You get all six dice back.")
            dice_list = dice_rolls(6)
        
        #print the current score and remaing dice
        print("Your current score in this turn is:", total_score)
        print("You have", len(dice_list), "dice to keep playing.")
        print()

    


def play_farkle():
    """ (NoneType) -> NoneType
    Executes a game of Farkle.
    """
    print("Welcome to COMP202_Farkle!")
    print()
    
    #asks how many players would like to play
    num_players = int(input("Please select the number of players (2-8): "))
    #if the input is not an integer between 2 and 8, asks for a new integer
    while num_players < 2 or num_players > 8:
        num_players = int(input("Please select the number of players (2-8): "))
        
    #asks for the wining score of this game
    winning_score = int(input("Select the wining score for this game: "))
    #if the input is not a positive integer, ask for a new integer
    while winning_score <= 0:
        winning_score = int(input("Select the wining score for this game: "))
    print()
    
    
    #create a list representing the score of each player
    score_list = []
    for i in range(num_players):
        score_list.append(0)
      
    round_num = 1
    
    #while there is no winner in this round, start a new round
    while max(score_list) < winning_score:
        
        #all the players take one turn
        for i in range(num_players):
            score_list[i] += play_one_turn(i+1)
        
        #displays the scores of all players
        print("After round", round_num, "the scores are as follows:")
        for i in range(num_players):
            print("Player", i+1, ":", score_list[i])
        print()
        
        round_num += 1
    
    #determine the winner of the game
    winner_list = get_winners(score_list, winning_score)
    winner = pick_random_element(winner_list)
    
    #display the winner
    print("Thank you for playing! The winner of this game is: Player ", winner)
    
    
    
    
    

#This module of program contains the functions that allow us to execute a game of Farkle,
#between mutiple players.
#Ziwei Hu 260889365
import random
from farkle_utils import *
 
#assign global variable to manipulate through the program
SINGLE_ONE = 100
SINGLE_FIVE = 50
TRIPLET_MULTIPLIER = 100
STRAIGHT = 3000
THREE_PAIRS = 1500
 
 
def compute_score(a_list):
    """ (list) -> int
    Returns the highest points scored of a_list, each element represents a 6-sided dice
    >>> compute_score([1,1,1])
    1000
    >>> compute_score([1,1,2,2,4,4])
    1500
    >>> compute_score([1,2,3,4,5,6])
    3000
    >>> compute_score([5,1,5,5])
    600
    >>> compute_score([1,1,3])
    0
    >>> compute_score([1,1,1,1,1,1])
    2000
    >>> compute_score([5,5,5,5,5,5])
    1500
    >>> compute_score([2,-1,2])
    Traceback (most recent call last)
    ValueError: The list should contain integers between 1 and 6.
    """
    #raise ValueError if the element is not integer between 1 and 6
    for element in a_list:
        if element < 1 or element > 6:
            raise ValueError("The list should contain integers between 1 and 6.")
        
    #create a variable score to add on
    score = 0
    
    #if a_list is 1 to 6, add STRAIGHT to score
    if contains_all(a_list) and len(a_list) == 6:
        score += STRAIGHT
        a_list = []
        
    #if a_list contains 3 pairs, and not all the elements equal to 1, add THREE_PAIRS
    #if all the elements equal to 1, mutiply the TRIPLET_MULTIPLIER by 20
    if count_num_of_pairs(a_list) == 3:
        if a_list == [1,1,1,1,1,1]:
            score += TRIPLET_MULTIPLIER * 20
            a_list = []
        else:
            score += THREE_PAIRS
            a_list = []
    
    #if there is three 1's in a_list, add score by mutipling the TRIPLET_MULTIPLIER by 10
    if contains_repetitions(a_list, 1, 3):
        score += TRIPLET_MULTIPLIER * 10
        a_list = get_difference(a_list,[1,1,1])
    
    #check if there is triplet from 2 to 6, if so, add score
    for i in range(2,7):
        if contains_repetitions(a_list, i, 3):
            score += TRIPLET_MULTIPLIER * i
            a_list = get_difference(a_list,[i,i,i])
         
    #while there is 1 in a_list, add score     
    while 1 in a_list:
        score += SINGLE_ONE
        a_list.remove(1)
    
    #while there is 5 in a_list, add score
    while 5 in a_list:
        score += SINGLE_FIVE
        a_list.remove(5)
    
    #if not all elements can be used to score, the total score is 0
    if len(a_list) > 0:
        score = 0
    
    return score
 
 
 
 
def get_winners(a_list, score_to_win):
    """ (list,int) -> list
    Returns a list of players with the highest score in a_list,
    which reached or surpassed score_to_win.
    >>> get_winners([500,1000,50],5000)
    []
    >>> get_winners([5000,10000,200],10000)
    [2]
    >>> get_winners([50,50,10,5],5)
    [1,2]
    >>> get_winners([50,-50,1],5)
    Traceback (most recent call last)
    ValueError: The list should contain all positive integers.
    >>> get_winners([1,2,3,4],-2)
    Traceback (most recent call last)
    ValueError: The winning score should be a positive integer.
    """
    #raise ValueError if there is non-positive integer in a_list
    for element in a_list:
        if element <= 0:
            raise ValueError("The list should contain all positive integers.")
        
    #raise ValueError if score_to_win is not positive
    if score_to_win <= 0:
        raise ValueError("The winning score should be a positive integer.")
    
    #create an empty list to add winner, get the maximum value in a_list
    winner_list = []
    highest_score = max(a_list)
    
    #if the highest score is lower than the score to win, returns empty string
    if highest_score < score_to_win:
        return winner_list
    
    #if there is any element equals to highest_score, appends its position to winner_list
    for i in range(len(a_list)):
        if a_list[i]                                                                                                               == highest_score:
            winner_list.append(i+1)
            
    return winner_list
            
            
        
        
def play_one_turn(player):
    """ (int) -> int
    Returns the score of player after they play this turn.
    """
    #raise ValueError if the number representing the play is non-positive
    if player <= 0:
        raise ValueError("The number of player should be a positive integer.")
    
    print("Player", player, "it's your turn!")
    print()
    
    #set the initial total score to 0, and the player starts with 6 dice
    total_score = 0
    dice_list = dice_rolls(6)
        
        
        
    #asks the user whether they would like to roll or pass
    #if the user still has dice remains
    while len(dice_list) != 0:
        
        user_decision = input("What would you like to do? (roll/pass): ")
        user_decision = user_decision.lower()
        
        #if the user chose not to roll, return the score
        if user_decision != "roll":
            print()
            return total_score
        
        
        #roll all the dice remaining again
        dice_list = dice_rolls(len(dice_list))
        
        #print the result of dice
        print("Here's the result of rolling your", len(dice_list),"dice:", end = " ")
        for i in range(len(dice_list)):
            dice_list[i] = str(dice_list[i])
        print(', '.join(dice_list))
        
        
        #asks the player to select the scoring dice to set aside
        user_selected = input("Please select the dice to set aside for scoring: ")
        scoring_dice = user_selected.split()
        
        #while the player selects dice that have not been rolled, asks again
        while not is_included(dice_list,scoring_dice):
            user_selected = input("You do not have these dice. Select again: ")
            scoring_dice = user_selected.split()
        
        #change all elements in lists to integer 
        for i in range(len(scoring_dice)):
            scoring_dice[i] = int(scoring_dice[i])
        
        for i in range(len(dice_list)):
            dice_list[i] = int(dice_list[i])
    
        #remove the asided scoring dice from original dice list
        dice_list = get_difference(dice_list, scoring_dice)
 
        
        #computes the current score and the remaining dice
        #if "farkled", all the points for this turn are lost
        score = compute_score(scoring_dice)
        if score == 0:
            total_score = 0
            dice_list += scoring_dice
            print("Farkle! All the points accumulated up to now are lost.")
        else:
            total_score += score
            
        #if there is no remaining dice, the player may continue their turn with new 6 dice
        if len(dice_list) == 0:
            print("HOT DICE! You are on a roll. You get all six dice back.")
            dice_list = dice_rolls(6)
        
        #print the current score and remaing dice
        print("Your current score in this turn is:", total_score)
        print("You have", len(dice_list), "dice to keep playing.")
        print()
 
    
 
 
def play_farkle():
    """ (NoneType) -> NoneType
    Executes a game of Farkle.
    """
    print("Welcome to COMP202_Farkle!")
    print()
    
    #asks how many players would like to play
    num_players = int(input("Please select the number of players (2-8): "))
    #if the input is not an integer between 2 and 8, asks for a new integer
    while num_players < 2 or num_players > 8:
        num_players = int(input("Please select the number of players (2-8): "))
        
    #asks for the wining score of this game
    winning_score = int(input("Select the wining score for this game: "))
    #if the input is not a positive integer, ask for a new integer
    while winning_score <= 0:
        winning_score = int(input("Select the wining score for this game: "))
    print()
    
    
    #create a list representing the score of each player
    score_list = []
    for i in range(num_players):
        score_list.append(0)
      
    round_num = 1
    
    #while there is no winner in this round, start a new round
    while max(score_list) < winning_score:
        
        #all the players take one turn
        for i in range(num_players):
            score_list[i] += play_one_turn(i+1)
        
        #displays the scores of all players
        print("After round", round_num, "the scores are as follows:")
        for i in range(num_players):
            print("Player", i+1, ":", score_list[i])
        print()
        
        round_num += 1
    
    #determine the winner of the game
    winner_list = get_winners(score_list, winning_score)
    winner = pick_random_element(winner_list)
    
    #display the winner
    print("Thank you for playing! The winner of this game is: Player ", winner)
    
    
    
    
    
 
 