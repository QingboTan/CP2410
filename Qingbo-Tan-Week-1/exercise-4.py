import random

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    print("binary search, list:", list, "item:", item)
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        print("low:", low)
        print("high:", high)
        print("guess:", guess)
        if guess == item:
            print("found item")
            return mid
        if guess > item:
            print("guess is greater than item")  # Corrected message
            high = mid - 1
        else:
            print("guess is less than item")
            low = mid + 1
    print("item not found")
    return None

my_list = [1, 3, 5, 7, 9]
print("result:", binary_search(my_list, 3))
print("result:", binary_search(my_list, -1))


# Generate a random sample of 1000 unique numbers from the range 1 to 99999
numbers = random.sample(range(1, 100000), 1000)

numbers.sort()  # Sort the list before performing binary search
print(binary_search(numbers, 42))
print(binary_search(numbers, 1000000))
print(binary_search(numbers, 1))
print(binary_search(numbers, 99999))
