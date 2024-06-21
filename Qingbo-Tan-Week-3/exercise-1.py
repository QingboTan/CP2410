from tail_recursive import tail_recursive
# def fibonacci(n):
#     """
#     Compute the nth Fibonacci number.
#     :param n: a non-negative integer
#     :return: the nth Fibonacci number
#     """
#     print("Computing fibonacci({})".format(n))
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#     # This algorithm has a time complexity of O(2^n) 
#     # Also known as "Exponential time"

# print(fibonacci(10))  # outputs: 55
# print(fibonacci(20))  # outputs: 6765
# print(fibonacci(30))  # outputs: 832040
# print(fibonacci(40))  # outputs: 102334155
# print(fibonacci(50))  # outputs: 12586269025

@tail_recursive()

def fibonacci(n, a=0, b=1):
    """ 
    Computes the nth Fibonacci number. 
    :param n: a positive integer 
    :param a: the first Fibonacci number 
    :param b: the second Fibonacci number 
    :return: the nth Fibonacci number itself 
    """
    # This function’s time complexity is O(n) linear time!
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci.tail_call(n - 1, b, a + b)

print(fibonacci(10))  # outputs: 55
print(fibonacci(20))  # outputs: 6765
print(fibonacci(30))  # outputs: 832040
print(fibonacci(40))  # outputs: 102334155
print(fibonacci(50))  # outputs: 12586269025