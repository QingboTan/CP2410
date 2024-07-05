def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return array


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    less = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    return quick_sort(less) + middle + quick_sort(greater)


import timeit
import random
import matplotlib.pyplot as plt


def run_benchmark(algorithm, data_list):
    return timeit.timeit(lambda: algorithm(data_list), number=10)


algorithms = {
    'Bubble Sort': bubble_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort
}

x = [length for length in range(1, 501, 50)]

# Average-case scenario
y_results_avg = {name: [] for name in algorithms.keys()}
for length in x:
    data_list = [random.randint(1, 100) for _ in range(length)]
    for name, algorithm in algorithms.items():
        result = run_benchmark(algorithm, data_list[:])
        y_results_avg[name].append(result)

# Plot average-case scenario
for name, results in y_results_avg.items():
    plt.plot(x, results, label=name)
plt.xlabel('n')
plt.ylabel('time (seconds)')
plt.title('Sorting Algorithms (Average Case)')
plt.legend()
plt.show()

# Worst-case scenario
y_results_worst = {name: [] for name in algorithms.keys()}
for length in x:
    data_list = [number for number in range(length, 0, -1)]
    for name, algorithm in algorithms.items():
        result = run_benchmark(algorithm, data_list[:])
        y_results_worst[name].append(result)

# Plot worst-case scenario
for name, results in y_results_worst.items():
    plt.plot(x, results, label=name)
plt.xlabel('n')
plt.ylabel('time (seconds)')
plt.title('Sorting Algorithms (Worst Case)')
plt.legend()
plt.show()