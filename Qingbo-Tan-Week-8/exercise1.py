import  random

with open("australian_cities.txt", "r") as f:
    australian_cities = eval(f.read())

print(australian_cities)

selected_cities = set(random.sample(sorted(australian_cities),10))

with open("selected_cities.txt","w") as file:
    file.write(str(selected_cities))

fictional_radio_stations = set()
for i in range(10):
    station_number = i + 1
    fictional_radio_stations.add(f"Radio Station {station_number:02}")

station_coverage = {}
for station in fictional_radio_stations:
    size = 8
    cities = sorted(selected_cities)
    station_coverage[station] = set(random.sample(cities,size))

with open("fictional_radio_stations.txt", "w") as file:
    file.write((str(fictional_radio_stations)))

with open("station_coverage.txt", "w") as file:
    file.write(str(station_coverage))

print("selected_cities:", sorted(selected_cities))
for station in sorted(station_coverage):
    print(f"{station} covers {sorted(station_coverage[station])}")