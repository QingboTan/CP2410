def is_palindrome(word):
    # Base case: A word with 0 or 1 character is always a palindrome
    if len(word) <= 1:
        return True
    # Check if the first and last characters are the same
    if word[0] == word[-1]:
        # If so, check if the rest of the word is a palindrome
        return is_palindrome(word[1:-1])
    else:
        # Otherwise the word is not a palindrome
        return False

print(is_palindrome("level"))     # outputs: True
print(is_palindrome("racecar"))   # outputs: True
print(is_palindrome("madam"))     # outputs: True
print(is_palindrome("12321"))     # outputs: True
print(is_palindrome("hello"))     # outputs: False

def is_palindrome_stack(word):
    stack = []
    # Push each character of the word onto the stack
    for char in word:
        stack.append(char)
    # Build the reversed word by popping characters from the stack
    reversed_word = ""
    while stack:
        reversed_word += stack.pop()
    # Compare the reversed word with the original word
    return word == reversed_word

print(is_palindrome_stack("level"))     # outputs: True
print(is_palindrome_stack("racecar"))   # outputs: True
print(is_palindrome_stack("madam"))     # outputs: True
print(is_palindrome_stack("12321"))     # outputs: True
print(is_palindrome_stack("hello"))     # outputs: False

# 5.each function's time complexity is.
# (is_palindrome)
# Time Complexity: O(n)

# (is_palindrome_stack)
# Time Complexity: O(n)
