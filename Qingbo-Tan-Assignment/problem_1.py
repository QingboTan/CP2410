import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

# Example usage:
n = 10
print(f"The smallest multiple for n = {n} is {smallest_multiple(n)}")
