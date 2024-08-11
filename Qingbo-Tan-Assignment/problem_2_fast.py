def nth_prime(n):
    limit = 10000000 #Initial estimate for the 10001st prime (could be adjusted)
    sieve = [True] * limit # Create a list of True values
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    count = 0
    for i in range(2, limit):
        if sieve[i]:  # If i is a prime
            count += 1
            if count == n:
                return i
            for j in range(i * i, limit, i):
                sieve[j] = False  # Mark multiples of i as non-prime

# Example usage:
n = 10001
print(f"The {n}th prime number is {nth_prime(n)}")

import time
import matplotlib.pyplot as plt
# Measure the time it takes to compute the smallest multiple for different values
times = []
ns = list(range(1, 10))  # You can increase this range

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
