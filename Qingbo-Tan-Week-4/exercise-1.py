import matplotlib.pyplot as plt
import math

# Set x-axis values
x = [length for length in range(1, 1001, 1)]

# Calculate y-axis values for different complexity functions
y_log_n = [math.log(n, 2) for n in x]
y_n = [n for n in x]
y_n_log_n = [n * math.log(n, 2) for n in x]
y_n_square = [n ** 2 for n in x]  # add this under the other lists

# Plot the graphs
plt.plot(x, y_log_n, label='log n')
plt.plot(x, y_n, label='n')
plt.plot(x, y_n_log_n, label='n*log n')
plt.plot(x, y_n_square, label='n^2')

# Set graph properties
plt.ticklabel_format(style='plain')
plt.ylim(0, 100)
plt.ylim(0, 1000)
plt.ylim(0, 100000)  # Set y-axis range
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Big O Notation')
plt.legend()
plt.show()