friends = {
    'Alice': ['Bob', 'Diane', 'Fred'], 
    'Bob': ['Alice', 'Cathy', 'Diane'], 
    'Cathy': ['Alice', 'Diane'], 
    'Diane': ['Alice', 'Fred'], 
    'Fred': [] 
}

def add_directed_edge(graph, source, destination):
# assume that the source and destination are in the graph
    graph[source].append(destination)

add_directed_edge(friends, 'Fred', 'Cathy')
print(friends)

def add_undirected_edge(graph, source, destination):
    # assume that the source and destination are in the graph
    add_directed_edge(graph, source, destination)
    add_directed_edge(graph, destination, source)

def add_node(graph, node):
    # assume taht node is not in the graph
    graph[node] = []
    
add_node(friends, 'Ginger')
add_undirected_edge(friends, 'Ginger', 'Fred')
print(friends)

def print_graph(graph):
    for node in graph:
        print(node, "->", graph[node])
   
def find_most_popular_friends(graph):
    largest_friendship_count = 0
    for node in graph:
        if len(graph[node]) > largest_friendship_count:
            largest_friendship_count = len(graph[node])
    most_popular = []
    for node in graph:
        if len(graph[node]) == largest_friendship_count:
            most_popular.append(node)
    return most_popular

print(find_most_popular_friends(friends))
#Question 1: Use the function to find Alice and Bob is most popular people
#Question 2: The maximum number will be 4
#Question 3: The complexity is O(n), each time run it takes O(n) but it takes twice
# so it will be O(2n), since in algorithm we usually do not count the constant, so
# in the end, it should be O(n)
