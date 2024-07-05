import matplotlib.pyplot as plt
import math

# Set x-axis values
x = [length for length in range(1, 21, 1)]  # Factorial grows very fast, so we limit n to 20

# Calculate y-axis values for different complexity functions
y_log_n = [math.log(n, 2) for n in x]
y_n = [n for n in x]
y_n_log_n = [n * math.log(n, 2) for n in x]
y_n_square = [n ** 2 for n in x]
y_2_n = [2 ** n for n in x]  # Exponential time
y_factorial = [math.factorial(n) for n in x]  # Factorial time

# Plot the graphs
plt.plot(x, y_log_n, label='log n')
plt.plot(x, y_n, label='n')
plt.plot(x, y_n_log_n, label='n*log n')
plt.plot(x, y_n_square, label='n^2')
plt.plot(x, y_2_n, label='2^n')
plt.plot(x, y_factorial, label='n!')

# Set graph properties
plt.ticklabel_format(style='plain')
plt.ylim(0, 1000)
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Big O Notation')
plt.legend()

# Show the plot
plt.show()