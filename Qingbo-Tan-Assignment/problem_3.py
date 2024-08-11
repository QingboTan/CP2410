def find_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a+1, n):
            c = n - a - b
            if a*a + b*b == c*c:
                return a, b, c
    return None

n = 1000
triplet = find_pythagorean_triplet(n)
if triplet:
    print(f"A Pythagorean triplet for n = {n} is {triplet}")
else:
    print(f"No Pythagorean triplet found for n = {n}")

import time
import matplotlib.pyplot as plt
# Measure the time it takes to compute the smallest multiple for different values
times = []
ns = list(range(1, 40))  # You can increase this range

for n in ns:
    start_time = time.time()
    find_pythagorean_triplet(n)  # can change here for different plot
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(ns, times, marker='o')
plt.xlabel('n')
plt.ylabel('Time(seconds)')
plt.title('Time to compute the nth prime number as a function of n')
plt.grid(True)
plt.show()