# Trade costs graph
trade_costs_graph = {
    'AlphaCo': {'BetaCorp': 5, 'GammaInc': 7.5, 'EpsilonPlc': 5},
    'BetaCorp': {'GammaInc': 4.5, 'DeltaLLC': 8},
    'GammaInc': {'BetaCorp': 4.5, 'DeltaLLC': 6},
    'DeltaLLC': {'EpsilonPlc': 9},
    'EpsilonPlc': {'AlphaCo': 14, 'GammaInc': 7}
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
            print(f"{start_node} --{weight}M$--> {end_node}")

# Iterate through each company and find shortest paths
for company in trade_costs_graph:
    costs, predecessors = dijkstra_algorithm(trade_costs_graph, company)
    shortest_paths = construct_shortest_paths(trade_costs_graph, predecessors)

    # Display the shortest paths graph for each company
    print(f"\nShortest Trading Paths for {company}:")
    display_graph(shortest_paths, trade_costs_graph)
