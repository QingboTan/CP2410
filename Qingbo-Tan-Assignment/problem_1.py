import math
import time
import matplotlib.pyplot as plt
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

#fast way O(nlogn)
def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
        # print(f'n={i}, result={result}')
    return result

#slow way O(n^3)
def smallest_multiple_slow(n):
    res = 1
    for i in range(1, n+1):   #O(n)
        res = res * i
        for test_res in range(2, res):  #O(n^2)
            found = True
            for test_i in range(2, i+1):  #O(n^3)
                if test_res % test_i != 0:
                    found = False
                    break
            if found:
                res = test_res
                break
    return res

# Example usage:
n = 10
print(f"The smallest multiple for n = {n} is {smallest_multiple(n)}")

print(smallest_multiple_slow(n))

# Measure the time it takes to compute the smallest multiple for different values
times = []
ns = list(range(1, 40))  # You can increase this range

for n in ns:
    start_time = time.time()
    smallest_multiple(n)  # can change here for different plot
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(ns, times, marker='o')
plt.xlabel('n')
plt.ylabel('Time(seconds)')
plt.title('Time to compute the smallest multiple as a function of n')
plt.grid(True)
plt.show()
