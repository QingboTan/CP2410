import random

def find_index_of_smallest(data_list): 
    if not data_list:
        return None
    smallest = data_list[0]
    for i in data_list:
        if i < smallest:
            smallest = i
    return data_list.index(smallest)

input_lists = [1, 2, 3, 0, 4, 5, 6, 7, 8, 0, 9, 10]
print(find_index_of_smallest(input_lists))

random_list = [random.randint(-100,100) for i in range(100000)]
print(find_index_of_smallest(random_list))
# This algorithm has a time complexity of O(n)

def find_indices_of_smallest(data_list):
    if not data_list:
        return []
    smallest = data_list[0]
    for i in data_list:
        if i < smallest:
            smallest = i
    indices = [index for index, value in enumerate(data_list) if value == smallest]
    return indices
# This algorithm has a time complexity of O(n)

test_data_1 = [4, 2, 7, 2, 5, 2]
test_data_2 = [1, 1, 1, 1]
test_data_3 = [10, 5, 3, 2, 2, 2]
test_data_4 = [5]
test_data_5 = []

print(find_indices_of_smallest(test_data_1))  # Output: [1, 3, 5]
print(find_indices_of_smallest(test_data_2))  # Output: [0, 1, 2, 3]
print(find_indices_of_smallest(test_data_3))  # Output: [3, 4, 5]
print(find_indices_of_smallest(test_data_4))  # Output: [0]
print(find_indices_of_smallest(test_data_5))  # Output: []