import timeit
import random
import matplotlib.pyplot as plt

def find_index_of_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    original_array = array[:]
    sorted_array = []
    for i in range(len(original_array)):
        smallest_index = find_index_of_smallest(original_array)
        sorted_array.append(original_array.pop(smallest_index))
    return sorted_array


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    less = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    return quick_sort(less) + middle + quick_sort(greater)


def run_benchmark(algorithm, data_list):
    return timeit.timeit(lambda: algorithm(data_list), number=10)

# Random data benchmark
x = [length for length in range(1, 1001, 10)]
y_selection_sort = []
y_quick_sort = []

for length in x:
    data_list = [random.randint(1, 100) for number in range(length)]
    result = run_benchmark(selection_sort, data_list[:])
    y_selection_sort.append(result)
    result = run_benchmark(quick_sort, data_list[:])
    y_quick_sort.append(result)

plt.plot(x, y_selection_sort, label='selection sort')
plt.plot(x, y_quick_sort, label='quick sort')
plt.ticklabel_format(style='plain')
plt.ylim(0, 0.1)  # You might need to adjust this
plt.xlabel('n')
plt.ylabel('time (seconds)')
plt.title('Running Times')
plt.legend()
plt.show()

# Worst-case scenario benchmark for quicksort
y_selection_sort_worst = []
y_quick_sort_worst = []

for length in x:
    data_list = [number for number in range(length)]
    result = run_benchmark(selection_sort, data_list[:])
    y_selection_sort.append(result)
    result = run_benchmark(quick_sort, data_list[:])
    y_quick_sort.append(result)

plt.plot(x, y_selection_sort_worst, label='selection sort (worst case)')
plt.plot(x, y_quick_sort_worst, label='quick sort (worst case)')
plt.ticklabel_format(style='plain')
plt.ylim(0, 0.1)  # You might need to adjust this
plt.xlabel('n')
plt.ylabel('time (seconds)')
plt.title('Running Times (Worst Case for Quicksort)')
plt.legend()
plt.show()