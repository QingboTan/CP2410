import itertools

from ast import literal_eval

with open('selected_cities.txt', 'r') as f:
    selected_cities = literal_eval(f.read())

with open('fictional_radio_stations.txt', 'r') as f:
    fictional_radio_stations = literal_eval(f.read())

with open('station_coverage.txt', 'r') as f:
    station_coverage = literal_eval(f.read())
print('selected_cities:', selected_cities)
print('fictional_radio_stations:', fictional_radio_stations)
print('station_coverage:', station_coverage)

cities_needed = selected_cities.copy()
print('cities_needed:', sorted(cities_needed))

def power_set(input_set):
    # base case: the empty set has only one subset, the empty set
    if len(input_set) == 0:
        return [[]]

    # recursion case: take an element from the set
    subsets = []
    first_element = input_set[0]
    for subset in power_set(input_set[1:]):
        subsets.append(subset)
        subsets.append([first_element] + subset)

    return subsets

# Generate all possible combinations of radio stations
all_subsets = []
for i in range(1, len(fictional_radio_stations) + 1):
    combination = itertools.combinations(fictional_radio_stations, i)
    all_subsets += list(combination)

# Print all combinations
print('all_subsets:', all_subsets)

# pick the smallest subset that covers all cities in cities_needed
best_stations = None
for subset in all_subsets:
    covered = set()
    for station in subset:
        covered |= station_coverage[station]
    if covered == cities_needed:
        best_stations = subset
    break

print('best stations: ', sorted(best_stations))

# print coverage cities from the best_stations
for station in sorted(best_stations):
    print(f'{station} covers {sorted(station_coverage[station])}')