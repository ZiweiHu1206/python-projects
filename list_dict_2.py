import doctest

def same_elements(a_list):
    """ (list) -> bool
    Returns True if all elements in each sublist are the same, False otherwise.
    >>> same_elements([[1,1,1],['a','a'],[6]])
    True
    >>> same_elements([[1,6,1],[6,6]])
    False
    """
    for sublist in a_list:
        first_element = sublist[0]
        for element in sublist:
            if element != first_element:
                return False
    return True
        
    
def flatten_list(a_list):
    """ (list) -> list
    Returns a 1D list containing all elements of the sublists of a_list
    >>> flatten_list([[1,2],[3],['a','b','c']])
    [1, 2, 3, 'a', 'b', 'c']
    >>> flatten_list([[]])
    []
    """
    new_list = []
    for sublist in a_list:
        for element in sublist:
            new_list.append(element)
            
    return new_list
    
    
def get_most_valuable_key(dictionary):
    """ (dict) -> str
    Returns the key which is mapped to the largest value.
    >>> get_most_valuable_key({'a': 3, 'b': 6, 'g': 0,'q': 9})
    'q'
    """
    num_list = []
    for key in dictionary:
        num_list.append(dictionary[key])
    
    largest_value = max(num_list)
    
    for key in dictionary:
        if dictionary[key] == largest_value:
            return key
    
    
def add_dicts(dict_1, dict_2):
    """ (dict,dict) -> dict
    Returns a dictionary which is a result of merging the two input dictionary
    >>> d1 = {'a':5, 'b':2, 'd':-1}
    >>> d2 = {'a':7, 'b':1, 'c':5}
    >>> add_dicts(d1, d2) == {'a':12, 'b':3, 'c':5, 'd':-1}
    True
    """
    for key in dict_2:
        if key in dict_1:
            dict_1[key] += dict_2[key]
        else:
            dict_1[key] = dict_2[key]
            
    return dict_1
    
    
def reverse_dict(d):
    """ (dict) -> dict
    Returns a dictionary where the values in d are now keys mapping to a list containing
    all keys in d which mapped to them.
    >>> a = reverse_dict({'a':3, 'b':2, 'c':3, 'd':5, 'e':2, 'f':3})
    >>> a == {3: ['a', 'c', 'f'], 2: ['b','e'], 5: ['d']}
    True
    """
    new_dict = {}
    d_items = d.items()
    list_of_tuples = list(d_items)
    for key, value in list_of_tuples:
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
    
    return new_dict
    
    
    
if __name__ == "__main__":
     doctest.testmod()