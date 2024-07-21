from exercise1 import display_graph
"""
difference between this fun, and find_min is this fun will go through all the path
in the weighted map, but find_min may not go through all the paths in order to find
the weight.
"""
def smallest_cost_node(nodes, costs):
    smallest_cost = float('inf')
    result = None
    for node in nodes:
        if costs[node] < smallest_cost:
            smallest_cost = costs[node]
            result = node
    return result

def construct_shortest_paths(graph,predecessors):
    shortest_paths = {}

    for node in predecessors:
        shortest_paths[node] = {}

    for node in predecessors:
        predecessor = predecessors[node]
        if predecessor is not None:
            shortest_paths[predecessor][node] = graph[predecessor][node]

    return shortest_paths


if __name__ == "__main__":
    weighted_graph = {}

    weighted_graph['A'] = {}
    weighted_graph['B'] = {}
    weighted_graph['C'] = {}
    weighted_graph['D'] = {}
    weighted_graph['E'] = {}
    weighted_graph['F'] = {}
    weighted_graph['G'] = {}
    weighted_graph['A']['B'] = 1
    weighted_graph['A']['C'] = 3
    weighted_graph['B']['C'] = 1
    weighted_graph['C']['E'] = 2
    weighted_graph['D']['F'] = 3
    weighted_graph['E']['B'] = 4
    weighted_graph['F']['E'] = 2
    weighted_graph['F']['G'] = 4

    costs = {}
    costs['A'] = 0
    costs['B'] = float('inf')
    costs['C'] = float('inf')
    costs['D'] = float('inf')
    costs['E'] = float('inf')
    costs['F'] = float('inf')
    costs['G'] = float('inf')
    """
        a. predecessor direct the shortest path way.
        b. Cost will keep changing until if find the shortest path,
        the infinity means can not get through.
    """

    predecessors = {}
    predecessors['A'] = None
    predecessors['B'] = None
    predecessors['C'] = None
    predecessors['D'] = None
    predecessors['E'] = None
    predecessors['F'] = None
    predecessors['G'] = None

    print(smallest_cost_node(['A', 'B', 'C'], {'A': 1, 'B': 2, 'C': 3})) # A
    print(smallest_cost_node(['A', 'B', 'C'], {'A': 3, 'B': 2, 'C': 1})) # C

    unvisited = set(weighted_graph.keys())

    while True:
        node = smallest_cost_node(unvisited,costs)
        if node is None:
            break

        unvisited.remove(node)

        for neighbour in weighted_graph[node]:
            alternative_cost = costs[node] + weighted_graph[node][neighbour]

            if alternative_cost < costs[neighbour]:
                costs[neighbour] = alternative_cost
                predecessors[neighbour] = node

    print(costs)
    print(predecessors)

    shortest_paths = construct_shortest_paths(weighted_graph, predecessors)
    display_graph(shortest_paths)
