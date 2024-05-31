import random

#1
def find_max(numbers):
    """
    This function returns the maximum number in a given list of numbers.
    Big-O running time: O(n) where n is the number of elements in the list. And It is linear. 
    """
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# 3-1: An empty list of numbers
print(find_max([]))

# 3-2: A list of the first 5 prime numbers, and search for an even number
prime_numbers = [2, 3, 5, 7, 11]
print(find_max(prime_numbers))

# 3-3: A list of numbers that are all the same, except for the very last number which is the maximum number in the list.
same_except_last = [2, 2, 2, 2, 3]
print(find_max(same_except_last))

# 3-4: A list of 10000 randomly selected numbers from the range 0 – 100 inclusive
random_numbers = [random.randint(0, 100) for _ in range(10000)]
print(find_max(random_numbers))

#4
def find_min(numbers):
    """
    This function returns the minimum number in a given list of numbers.
    Big-O running time: O(n) where n is the number of elements in the list.
    """
    if not numbers: #handle empty list case
        return None
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

# 1
print(find_min([]))

# 2
prime_numbers = [2, 3, 5, 7, 11]
print(find_min(prime_numbers))

# 3
same_except_last = [3, 3, 3, 3, 2]
print(find_min(same_except_last))

# 4
print(find_min(random_numbers))

# They are all O(n)
