def find_index_of_smallest(data_list): 
    smallest = data_list[0]
    for i in data_list:
        if i < smallest:
            smallest = i
    return data_list.index(smallest)

