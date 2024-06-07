def binary_search(data_list, target):
    if not data_list:
        return None
    low = 0
    high = len(data_list)
    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] < target:
            low = mid + 1
        elif data_list[mid] > target:
            high = mid - 1
        else:
            return mid
    return None

print(binary_search([], 42))  # outputs: None
print(binary_search([1, 2, 3, 4, 5], 3))  # outputs: 2
print(binary_search([1, 2, 3, 4, 5], 6))  # outputs: None
print(binary_search([1, 2, 3, 4, 5], 0))  # outputs: None