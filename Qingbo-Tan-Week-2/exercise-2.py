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