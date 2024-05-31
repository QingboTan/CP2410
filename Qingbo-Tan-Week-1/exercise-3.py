def calculate_average(numbers):
    count = 0
    for number in numbers:
        count += number
    average_number = count/len(numbers)
    return average_number

numbers = [1,2,3,4,5,6,7,8]
print(calculate_average(numbers))
