def find_smallest(data_list): 
    """
    Find the smallest element in a list
    :param data_list: a list of elements
    :return: smallest element
    """
    smallest = data_list[0]
    for i in data_list:
        if i < smallest:
            smallest = i
    return smallest

# This algorithm has a time complexity of O(n)

print(find_smallest([1, 2, -8, 0, 5, 6, 10])) # outputs: -8 
print(find_smallest([1, 2, -8, 0, 5, 6, 10, -100])) # outputs: -100
 