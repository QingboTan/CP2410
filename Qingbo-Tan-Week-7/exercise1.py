def display_graph(graph):
    for node in graph:
        for neighbour in graph[node]:
            print(f"{node} -- {graph[node][neighbour]} -> {neighbour}")
        print()


def find_reachable_node(graph,node):
    reachable_nodes = set()
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        reachable_nodes.add(current_node)
        for neighbour in graph[current_node]:
            if neighbour not in reachable_nodes and neighbour not in queue:
                queue.append(neighbour)
    reachable_nodes.remove(node)
    return reachable_nodes


def is_part_of_cycle(graph,node):
    reachable_from_node = find_reachable_node(graph,node)
    for reachable_node in reachable_from_node:
        if node in find_reachable_node(graph,reachable_node):
            return True
    return False

if __name__ == "__main__":
    weight_graph = {}

    weight_graph["A"] = {}
    weight_graph["B"] = {}
    weight_graph["C"] = {}
    weight_graph["D"] = {}
    weight_graph["E"] = {}
    weight_graph["F"] = {}
    weight_graph["G"] = {}

    weight_graph["A"]["B"] = 1
    weight_graph["A"]["C"] = 3
    weight_graph["B"]["C"] = 1
    weight_graph["B"]["D"] = 2
    weight_graph["C"]["E"] = 2
    weight_graph["D"]["F"] = 3
    weight_graph["E"]["B"] = 4
    weight_graph["F"]["E"] = 2
    weight_graph["F"]["G"] = 4
    weight_graph["B"].pop("D")

    display_graph(weight_graph)
    for node in weight_graph:
        reachable_nodes = find_reachable_node(weight_graph, node)
        print(f"{node} can reach: {reachable_nodes}")

    for node in weight_graph:
        """
        if is_part_of_cycle:
            status = "yes"
        else:
            status = "no"
        """
        status = "yes" if is_part_of_cycle(weight_graph,node) else "no"#Short-cut
        print(f"Is {node} part of a cycle: {status}")