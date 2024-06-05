names = []
ids = []

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

    with open("student_data.txt") as file:
        next(file)  # skip headers
        for line in file:
            parts = line.strip().split(",")
            names.append(parts[0])
            ids.append(int(parts[1]))

# Ensure ids are sorted for binary search
sorted_indices = sorted(range(len(ids)), key=lambda i: ids[i])
ids = [ids[i] for i in sorted_indices]
names = [names[i] for i in sorted_indices]

val = input("Enter your student id: ")
index = binary_search(ids, int(val))
if index is not None:
    print(f"Student Name: {names[index]}")
else:
    print("Student ID not found")
