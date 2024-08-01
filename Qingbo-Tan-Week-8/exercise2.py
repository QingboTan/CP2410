import itertools
from ast import literal_eval

# Load data from files
with open('selected_cities.txt', 'r') as f:
    selected_cities = literal_eval(f.read())

with open('fictional_radio_stations.txt', 'r') as f:
    fictional_radio_stations = literal_eval(f.read())

with open('station_coverage.txt', 'r') as f:
    station_coverage = literal_eval(f.read())

# Setup the "cities_needed" variable
cities_needed = selected_cities.copy()
print('cities_needed:', sorted(cities_needed))

# Approximation algorithm for computing a set-cover
selected_stations = set()
while cities_needed:
    best_station = None
    cities_covered = set()
    # Search for the next best station
    for station, cities_for_station in station_coverage.items():
        covered = cities_needed & cities_for_station
        if len(covered) > len(cities_covered):  # a "good" station
            best_station = station
            cities_covered = covered
    cities_needed -= cities_covered  # remove cities we have covered
    selected_stations.add(best_station)  # select this "good" station

# Print out the results
print('best stations: ', sorted(selected_stations))
# Print coverage cities from the selected_stations
for station in sorted(selected_stations):
    print(f'{station} covers {sorted(station_coverage[station])}')
