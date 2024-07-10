# Define a cache for factorial results
factorial_cache = {}


# Define the factorial function
def factorial(n):
    # If n is 0 or 1, return 1 since 0! = 1! = 1
    if n == 0 or n == 1:
        return 1

    # If we calculated factorial(n) before, return the cached value
    if n in factorial_cache:
        print("using cached factorial of", n)
        return factorial_cache[n]

    # Otherwise, calculate factorial(n) and store it in the cache
    else:
        print("not using cached factorial of", n)
        result = n * factorial(n - 1)
        factorial_cache[n] = result
        return result


# Test cases for the cached implementation of factorial
print(factorial(5))
print(factorial(3))
