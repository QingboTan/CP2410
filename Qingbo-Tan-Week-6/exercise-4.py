from exercise1 import add_directed_edge, add_node, add_undirected_edge, print_graph, find_most_popular_friends

if __name__ == '__main__':
    friends = {
        'Alice': ['Bob', 'Diane', 'Fred'],
        'Bob': ['Alice', 'Cathy', 'Diane'],
        'Cathy': ['Alice', 'Diane'],
        'Diane': ['Alice', 'Fred'],
        'Fred': []
        }
    add_directed_edge(friends, 'Fred', 'Cathy')
    print(friends)
    add_node(friends, 'Ginger')
    add_undirected_edge(friends, 'Ginger', 'Fred')
    print(friends)
    print_graph(friends)
    print(find_most_popular_friends(friends))

file = open("social_network_5.txt")
graph = eval(file.read())
file.close()
print_graph(graph)

queue = []
queue.append("Wayne")

visited = []
step = 1
while queue:
    node = queue.pop(0)
    print("dequeue", node)

    if node not in visited:
        visited.append(node)
        print("visiting", node)

        level = []
        for neighbour in graph[node]:
            if neighbour not in queue and neighbour not in visited:
                print("enqueue", neighbour)
                queue.append(neighbour)
                level.append(neighbour)
        if level:
            level.append(level)
    print("step {} completed. queue: {} visited: {}".format(step, queue, visited))
    step += 1

print("levels",level)
