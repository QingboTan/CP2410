def is_prime(num):
    if num <= 1: #prime number has to be positive
        return False
    if num == 2: #start from 2
        return True
    if num % 2 == 0: #prime number cannot be even
        return False
    for i in range(3, n, 2): #check odd number from 3(first odd number) to n
        if num % i == 0: #check if prime number is divisible by'i'
            return False
    return True

def nth_prime(n):
    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1

# Example usage:
n = 10001
print(f"The {n}th prime number is {nth_prime(n)}")

import time
import matplotlib.pyplot as plt
# Measure the time it takes to compute the smallest multiple for different values
times = []
ns = list(range(1, 40))  # You can increase this range

for n in ns:
    start_time = time.time()
    nth_prime(n)  # can change here for different plot
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(ns, times, marker='o')
plt.xlabel('n')
plt.ylabel('Time(seconds)')
plt.title('Time to compute the nth prime number as a function of n')
plt.grid(True)
plt.show()
