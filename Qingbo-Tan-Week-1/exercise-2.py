def find_max(numbers):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

numbers = [5,10,7,8,23,3]
print(find_max(numbers))



