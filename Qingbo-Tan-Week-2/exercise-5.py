def binary_search(student_id, filename):
    with open(filename, "rb") as file:  # Read the number of student records from the first 4 bytes
        file.seek(0)
        num_records_bytes = file.read(4)
        num_records = int.from_bytes(num_records_bytes, byteorder='big')

    # Set initial values for binary search
    low = 0
    high = num_records - 1

    while low <= high:
        mid = (low + high) // 2
        offset = mid * 21 + 4 # Each student record is 21 bytes, plus 4 bytes for the count

    # Move to the middle record and read its student ID
    file.seek(offset + 11) # Jump to the ID part of the record
    record_id = file.read(10).decode('utf-8')

    if record_id == student_id: # Found the ID, retrieve the corresponding name
        file.seek(offset) # Jump back to the start of the record to get the name
        record = file.read(21)
        student_name = record[0:11].decode('utf-8').strip()
        return student_name

    elif record_id < student_id:
        low = mid + 1 # Search the right half of the remaining records

    else:
        high = mid - 1 # Search the left half of the remaining records

    return None # Student ID not found

# Test cases
print(binary_search("0000000064", "student_data.bin")) # Output: Matthew
print(binary_search("0000001447", "student_data.bin")) # Output: Timothy
print(binary_search("0000030899", "student_data.bin")) # Output: Anthony
print(binary_search("5049830265", "student_data.bin")) # Output: Steven