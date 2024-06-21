def is_balanced_v1(string):
    return string.count("(") == string.count(")")

print("version 1 - not recursive - using count()")
print(is_balanced_v1("("))  # outputs: False
print(is_balanced_v1("()"))  # outputs: True
print(is_balanced_v1(")("))  # outputs: True but that's wrong!
print(is_balanced_v1("()()"))  # outputs: True

def is_balanced_v2(string):
    if len(string) == 0:
        return True
    elif string[0] == "(" and string[-1] == ")":
        return is_balanced_v2(string[1:-1])
    else:
        return False
print("version 2 - recursive - using string slicing")
print(is_balanced_v2("("))  # outputs: False
print(is_balanced_v2("()"))  # outputs: True
print(is_balanced_v2("(())"))  # outputs: True
print(is_balanced_v2(")("))  # outputs: False
print(is_balanced_v2("()()"))  # outputs: False but that's wrong!
print(is_balanced_v2("()(())"))  # outputs: False but that's wrong!

def is_balanced_v3(string):
    counter = 0
    for char in string:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0
print("version 3 - not recursive - using a counter")
print(is_balanced_v3("("))  # outputs: False
print(is_balanced_v3("()"))  # outputs: True
print(is_balanced_v3("(())"))  # outputs: True
print(is_balanced_v3(")("))  # outputs: False
print(is_balanced_v3("()()"))  # outputs: True
print(is_balanced_v3("()(())"))  # outputs: True
print(is_balanced_v3("()(()))"))  # outputs: False
print(is_balanced_v3("(()(()))"))  # outputs: True

def is_balanced_v4(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
print("version 4 - not recursive - using a stack")
print(is_balanced_v4("("))  # outputs: False
print(is_balanced_v4("()"))  # outputs: True
print(is_balanced_v4("(())"))  # outputs: True
print(is_balanced_v4(")("))  # outputs: False
print(is_balanced_v4("()()"))  # outputs: True
print(is_balanced_v4("()(())"))  # outputs: True
print(is_balanced_v4("()(()))"))  # outputs: False
print(is_balanced_v4("(()(()))"))  # outputs: True

# 5.Create a small program that uses versions 3 & 4 of is_balanced().
def main():
    user_input = input("Enter a string of parentheses to check if it's balanced ")
    print("Using version 3 - Counter method:")
    print(is_balanced_v3(user_input))
    print("Using version 4 - Stack method:")
    print(is_balanced_v4(user_input))

main()

# 6.each function's time complexity is.
# Version 1: O(n)
# Version 2: O(n^2)
# Version 3: O(n)
# Version 4: O(n)
