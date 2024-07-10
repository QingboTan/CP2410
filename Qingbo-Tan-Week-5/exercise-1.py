def recursive_fib(n):
    if n <= 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)

# print(recursive_fib(1000)) # This will cause a "call stack overflow"

def cached_fib(n, cache=None):
    """  
    Return the nth Fibonacci number. 
    :param n: the index of the Fibonacci number to be returned 
    :param cache: previously computed numbers 
    """
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]
    elif n <= 1:
        return n
    else:
        cache[n] = cached_fib(n - 1, cache) + cached_fib(n - 2, cache)
        return cache[n]

# Test with a large Fibonacci number
print(cached_fib(1000))

# Question Answer
# Using the cached Fibonacci function cached_fib() typically avoids "call stack overflow" by reusing previously computed Fibonacci numbers.
# However, for very large n, it can still be affected by Python's recursion depth limit. The efficiency of cached_fib() depends on effective caching and recursion depth.
# While it generally improves performance, extremely large n values can still cause issues. Despite computing each Fibonacci number once and caching it, the time complexity is not strictly O(n).