import doctest


def count_characters(a_string):
    """ (str) -> dict
    Returns a dictionary that count the number of occurrence of each character in a_string.
    >>> count_characters("banana")
    {'b': 1, 'a': 3, 'n': 2}
    """
    char_counting = dict()
    for char in a_string:
        if char not in char_counting:
            char_counting[char] = 1
        else:
            char_counting[char] += 1
    return char_counting


def merge_inventory(inventory_one, inventory_two):
    """ (dict,dict) -> dict
    Returns a dictionary that combine inventory_one and inventory_two
    representing the entire inventory of the company
    >>> inventory_one = {"sofa":5, "chair":12, "lamp":3}
    >>> inventory_two = {"sofa":1, "area rug":6, "coffe_table":2, "lamp":5}
    >>> d = merge_inventory(inventory_one, inventory_two)
    >>> len(d)
    5
    """
    for key in inventory_one:
        if key not in inventory_two:
            inventory_two[key] = inventory_one[key]
        else:
            inventory_two[key] += inventory_one[key]
    return inventory_two
    
    
    
def reverse_lookup(d,target):
    """ (dict,int) -> list
    Returns the list of keys in d that maps to target.
    >>> k = reverse_lookup({'a':3, 'b':2, 'c':3, 'd':5, 'e':0, 'f':3}, 3)
    >>> k == ['a', 'c', 'f']
    True
    >>> reverse_lookup({'a':3, 'b':2, 'c':3, 'd':5, 'e':0, 'f':3},1)
    []
    """
    list_of_keys = []
    for key in d:
        if d[key] == target:
            list_of_keys.append(key)
            
    return list_of_keys
            
            
def get_max_value(d):
    """ (dict) -> int
    Returns the largest value in the d.
    >>> get_max_value({'a':3, 'b':2, 'c':3, 'd':5, 'e':0, 'f':3})
    5
    """
    value_list = []
    for key in d:
        value_list.append(d[key])
        
    if len(d) == 0:
        return None
    
    largest_value = max(value_list)
    
    return largest_value
     



if __name__ == "__main__":
    doctest.testmod()