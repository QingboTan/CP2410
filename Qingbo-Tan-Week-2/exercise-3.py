def find_index_of_smallest(data_list):
    if not data_list:
        return None
    smallest = data_list[0]
    for i in data_list:
        if i < smallest:
            smallest = i
    return data_list.index(smallest)

def selection_sort(data_list):
    """
    Sort a list using selection sort. Time complexity: O(n^2)
    :param data_list: a list of elements
    :return: sorted list
    """
    if not data_list:
        return None
    sorted_list = []
    for i in range(len(data_list)):
        smallest_index = find_index_of_smallest(data_list)
        sorted_list.append(data_list.pop(smallest_index))
    return sorted_list

print(selection_sort([64, 25, 12, 22, 11])) # Expected output: [11, 12, 22, 25, 64]
print(selection_sort([5, 3, 6, 2, 10]))    # Expected output: [2, 3, 5, 6, 10]
print(selection_sort([]))                  # Expected output: []
print(selection_sort([1]))                 # Expected output: [1]
print(selection_sort([2, 1]))              # Expected output: [1, 2]
print(selection_sort([1, 2, 3, 4, 5]))     # Expected output: [1, 2, 3, 4, 5]
