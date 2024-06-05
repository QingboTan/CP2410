def selection_sort(data_list): 
    """
    Sort a list using selection sort. Time complexity: _______
    :param data_list: a list of elements
    :return: sorted list
    """
    if not data_list:
        return ______
    sorted_list = ______
    for i in range(len(data_list)):
        __________ = ______________________________
        sorted_list.append(data_list.pop(smallest_index))
    return sorted_list