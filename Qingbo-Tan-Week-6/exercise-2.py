from pyvis.network import Network

# load graph from file
file = open('social_network_5.txt', 'r')
graph = eval(file.read()) # convert the text into a dictionary
file.close()

# use Pyvis to draw a graph with directed edges
net = Network(directed=True)
# add the nodes to the Pyvis network from the raw graph
for node in graph:
    net.add_node(node)
# add the edges to the Pyvis network from the raw graph
for node in graph:
    for edge in graph[node]:
        net.add_edge(node, edge)

net.save_graph('social_network.html')

file = open('social_network_50.txt','r')
# net = Network(directed=True)
net = Network(directed=True, select_menu=True, filter_menu=True)

net.show_buttons(filter_=['physics'])
net.repulsion(node_distance=500)
net.save_graph('social_network.html')
