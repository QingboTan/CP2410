import math

def find_least_popular_friends(graph):
    smallest_friendship_count = math.inf # math.inf represent positive infinity
    for node in graph:
        if len(graph[node]) < smallest_friendship_count:
            smallest_friendship_count = len(graph[node])
    least_popular = []
    for node in graph:
        if len(graph[node]) == smallest_friendship_count:
            least_popular.append(node)
    return least_popular

with open("social_network_5.txt", "r") as file:
    graph = eval(file.read())
    print(find_least_popular_friends(graph))

with open("social_network_50.txt", "r") as file:
    graph = eval(file.read())
    print(find_least_popular_friends(graph))


"1, Ernest"
