#This program implements a simple version of Conway's Game of Life.
#Ziwei Hu 
 
 
def is_valid_universe(universe_list):
    """ (list) -> bool
    Returns True if universe_list is a valid representation of a universe, False otherwise.
    
    >>> a = [[0,0], [1,0], [1,0]]
    >>> is_valid_universe(a)
    True
    
    >>> b = [[0,0,1],[0,1],[1]]
    >>> is_valid_universe(b)
    False
    
    >>> c = [[1,3],[5,4]]
    >>> is_valid_universe(c)
    False
    
    >>> d = [[],[]]
    >>> is_valid_universe(d)
    False
    
    >>> e = []
    >>> is_valid_universe(e)
    False
    """
    #if the a_list is empty, return False
    if len(universe_list) == 0:
        return False
    
    #if any sublist in a_list is empty, return False
    for sublist in universe_list:
        if len(sublist) == 0:
            return False
 
    #iterate through each sublist to check its length is equal to another
    for sublist in universe_list:
        if len(sublist) != len(universe_list[0]):
            return False
    
    #iterate through each element in each sublist, if not equal to 0 or 1, return False
    for sublist in universe_list:
        for element in sublist:
            if element != 0 and element != 1:
                return False
    
    return True
    
    
    
def universe_to_str(universe_list):
    """ (list) -> str
    Returns the string representation of universe_list.
    
    >>> a = [[0,0,1,0],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
    >>> str_a = universe_to_str(a)
    >>> print(str_a)
    +----+
    |  * |
    |  **|
    |****|
    |    |
    +----+
    
    >>> b = [[0,0,0,0,0,0],[1,0,0,0,0,1],[1,0,0,0,0,1]]
    >>> str_b = universe_to_str(b)
    >>> print(str_b)
    +------+
    |      |
    |*    *|
    |*    *|
    +------+
    
    >>> c = [[1,1,1],[1,0,0]]
    >>> str_c = universe_to_str(c)
    >>> print(str_c)
    +---+
    |***|
    |*  |
    +---+
    """
    #calculate the length of sublist in universe_list
    len_sublist = len(universe_list[0])
    
    #create the first line of the string representation of universe_list
    str_representation = "+" + ("-" * len_sublist) + "+\n"
    
    
    #iterate through every element in each sublist of universe_list
    #to create the actual cells of the universe with "|" around
    for sublist in universe_list:
        str_representation += "|"
    
        for element in sublist:
            if element == 1:
                str_representation += "*"
            else:
                str_representation += " "
        
        str_representation += "|\n"
        
        
    #add the last line of string representation to close the box
    str_representation += "+" + ("-" * len_sublist) + "+"
    
    return str_representation
    
 
 
def count_live_neighbors(universe_list, x, y):
    """ (list,int,int) -> int
    Returns the number of live neighboring cells to the cell at location of x and y
    
    >>> a = [[0,0,0,0],\
             [0,1,0,0],\
             [1,1,1,1]]
    >>> count_live_neighbors(a, 0, 1)
    1
    >>> count_live_neighbors(a, 1, 2)
    4
    
    >>> b = [[0,0,1,0,0],\
             [1,0,1,0,1],\
             [1,0,0,0,1]]
    >>> count_live_neighbors(b, 0, 1)
    3
    >>> count_live_neighbors(b, 2, 3)
    3
    """
    num_live_neighbors = 0
    
    #check through each element surround the given cell
    #if it is equal to 1, increase num_live_neighbors by 1
    #check the left, upper and lower left elements of the given cell
    if x-1 >= 0 and y-1 >= 0: 
        if universe_list[x-1][y-1] == 1:
            num_live_neighbors += 1
    
    if y-1 >= 0:
        if universe_list[x][y-1] == 1:
            num_live_neighbors += 1
            
    if x+1 < len(universe_list) and y-1 >= 0:
        if universe_list[x+1][y-1] == 1:
            num_live_neighbors += 1
        
    #check the upper and lower elements of the given cell
    if x-1 >= 0:
        if universe_list[x-1][y] == 1:
            num_live_neighbors += 1
    
    if x+1 < len(universe_list):
        if universe_list[x+1][y] == 1:
            num_live_neighbors += 1
        
    #check the right, upper right, and lower right elements of the given cell
    if x-1 >= 0 and y+1 < len(universe_list[0]):
        if universe_list[x-1][y+1] == 1:
            num_live_neighbors += 1
    
    if y+1 < len(universe_list[0]):
        if universe_list[x][y+1] == 1:
            num_live_neighbors += 1
    
    if x+1 < len(universe_list) and y+1 < len(universe_list[0]):
        if universe_list[x+1][y+1]==1:
            num_live_neighbors += 1
    
    return num_live_neighbors
        
 
 
def get_next_gen_cell(universe_list, x, y):
    """ (list,int,int) -> int
    Returns the state of the specified cell in the next generation of the universe,
    1 is returned if such cell will be alive in the next generation, 0 otherwise.
    
    >>> a = [[0,0,0,0],\
             [0,0,1,1],\
             [0,1,0,0],\
             [0,0,1,1]]
    >>> get_next_gen_cell(a, 1, 2)
    1
    >>> get_next_gen_cell(a, 3, 0)
    0
    
    >>> b = [[0,0,0,0,0],\
             [0,1,1,1,1],\
             [0,1,0,1,0]]
    >>> get_next_gen_cell(b, 1, 1)
    1
    >>> get_next_gen_cell(b, 1, 2)
    0
    >>> get_next_gen_cell(b, 0, 3)
    1
    """
    #determine the next generation state if the cell is alive
    if universe_list[x][y] == 1:
        
        #the cell dies with fewer than two live neighbors
        if count_live_neighbors(universe_list, x, y) < 2:
            return 0
        
        #the cell lives on to the next generation with two or three live neighbors
        if 2 <= count_live_neighbors(universe_list, x, y) < 4:
            return 1
        
        #the cell dies with more than three live neighbors
        if count_live_neighbors(universe_list, x, y) > 3:
            return 0
    
    
    #determine the next generation state if the cell is died
    if universe_list[x][y] == 0:
        
        #the cell becomes a live cell with three live neighbors
        if count_live_neighbors(universe_list, x, y) == 3:
            return 1
        else:
            return 0
        
 
 
def get_next_gen_universe(universe_list):
    """ (list) -> list
    Returns a 2D list of integers representing the universe in its next generation.
    
    >>> a = [[0,0,0,0,0],[0,0,1,0,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]
    >>> get_next_gen_universe(a)
    [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    
    >>> b = [[0,1,1,1,0],[0,0,1,1,1],[0,0,0,0,0]]
    >>> get_next_gen_universe(b)
    [[0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 0, 0, 1, 0]]
    
    >>> c = [[1,1,1,1,1],[1,1,0,1,0],[1,1,0,0,0]]
    >>> get_next_gen_universe(c)
    [[1, 0, 0, 1, 1], [0, 0, 0, 1, 1], [1, 1, 1, 0, 0]]
    """
    #create a deep copy of universe_list
    copy_list = []
    for sublist in universe_list:
        new_sublist = []
        for element in sublist:
            new_sublist.append(element)
        copy_list.append(new_sublist)
    
    
    #iterate through every element in each sublist of universe_list
    #determine the state of each cell's next generation
    for x in range(len(universe_list)):
        for y in range(len(universe_list[0])):
            universe_list[x][y] = get_next_gen_cell(copy_list, x, y)
    
    return universe_list
 
 
 
def get_n_generations(a_list, n):
    """ (list,int) -> list
    Returns a list containing m strings which represent the first m generations of
    the input universe.
    
    >>> blinker = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    >>> g = get_n_generations(blinker, 4)
    >>> len(g)
    2
    >>> g[0] == universe_to_str(blinker)
    True
    
    >>> beacon = [[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,1,1,0],\
                  [0,0,0,0,0,0]]
    >>> g = get_n_generations(beacon, 6)
    >>> len(g)
    2
    >>> print(g[1])
    +------+
    |      |
    | **   |
    | *    |
    |    * |
    |   ** |
    |      |
    +------+
    
    >>> block = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    >>> g = get_n_generations(block, 10)
    >>> len(g)
    1
    >>> g[0] == universe_to_str(block)
    True
    """
    #raise TypeError if a_list and n are not the correct type
    if type(a_list) != list:
        raise TypeError("The first input should be a list.")
    if type(n) != int:
        raise TypeError("The second input should be an integer.")
    
    #raise ValueError if the first input does not represent a valid universe
    if not is_valid_universe(a_list):
        raise ValueError("The first input should be a valid universe.")
    
    #raise ValueError if the second input is not a positive number greater than 0
    if n <= 0:
        raise ValueError("The second input should be a positive number greater than 0.")
    
    
    #create an empty list                                                         
    n_generations_list = []
    
    #get n generations of a_list
    #convert to each generation to its string representation, add to n_generation_list
    while len(n_generations_list) < n:
        str_representation = universe_to_str(a_list)
        n_generations_list.append(str_representation)
        a_list = get_next_gen_universe(a_list)
       
    
    #check if the universe is periodic, if is, get the period of universe
    for index in range(1, len(n_generations_list)):
        if n_generations_list[index] == n_generations_list[0]:
            period_universe = index
            break
    
    #get the minimum number between n and period_universe
    m = min(n, period_universe)
    
    #slice generation_list from first element to m element and add it to a new list
    m_generations_list = n_generations_list[:m]
    
    return m_generations_list
 