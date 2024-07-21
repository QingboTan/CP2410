# Define the weighted graph
weighted_graph = {
    'New York': {'Los Angeles': 27.4, 'Chicago': 7.18},
    'Los Angeles': {},
    'Chicago': {'Houston': 10.89},
    'Houston': {'Phoenix': 11.62},
    'Phoenix': {'Los Angeles': 3.75},
    'Philadelphia': {'New York': 0.95, 'Chicago': 7.59}
}

# Dijkstra's algorithm implementation
def dijkstra_algorithm(graph, start_node):
    costs = {node: float('inf') for node in graph}
    costs[start_node] = 0
    predecessors = {node: None for node in graph}
    unvisited = set(graph.keys())

    while unvisited:
        current_node = min(unvisited, key=lambda node: costs[node])
        unvisited.remove(current_node)

        for neighbour, weight in graph[current_node].items():
            alternative_cost = costs[current_node] + weight
            if alternative_cost < costs[neighbour]:
                costs[neighbour] = alternative_cost
                predecessors[neighbour] = current_node

    return costs, predecessors

# Function to construct shortest paths graph
def construct_shortest_paths(graph, predecessors):
    shortest_paths = {}
    for node, predecessor in predecessors.items():
        if predecessor is not None:
            if predecessor not in shortest_paths:
                shortest_paths[predecessor] = {}
            shortest_paths[predecessor][node] = graph[predecessor][node]
    return shortest_paths

# Function to display a graph
def display_graph(graph, weighted_graph):
    for start_node in graph:
        for end_node in graph[start_node]:
            weight = weighted_graph[start_node][end_node]
            print(f"{start_node} --{weight}-> {end_node}")

# Compute shortest paths from New York
costs, predecessors = dijkstra_algorithm(weighted_graph, 'New York')

# Construct the shortest paths graph
shortest_paths = construct_shortest_paths(weighted_graph, predecessors)

# Display Costs and Predecessors
print("Costs and predecessors for each node in the graph:")
print("Costs:")
for node, cost in costs.items():
    print(f"{node}: {cost}")
print("\nPredecessors:")
for node, predecessor in predecessors.items():
    print(f"{node}: {predecessor}")

# Display the shortest paths graph
print("\nA graph representing the shortest paths from New York to all reachable cities:")
display_graph(shortest_paths, weighted_graph)
