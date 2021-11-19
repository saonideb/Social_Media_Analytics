import networkx as nx
import igraph
import matplotlib.pyplot as plt

# read the dataset using igraph module
temp_graph = igraph.read("karate.gml")

# for each edge, get a list of pairs of integers (a, b) where a = the source vertex ID and b =  the target vertex ID
another_graph = temp_graph.get_edgelist()

# creates a graph suitable for networkx module
our_graph = nx.Graph(another_graph)
print(our_graph)

# visualize the graph
nx.draw(another_graph, with_labels=True)


# this function first calculates the edge betweenness centrality and then returns the edge with the highest EBC score.
# this is done because in Girvan Newman Algorithm, we take out the edges one by one based on the EBC score starting
# with the edge having the highest EBC score.
def edge_to_be_removed(input_graph):
    # calculate the edge betweeness centrality
    graph_dictionary = nx.edge_betweenness_centrality(input_graph)
    set_of_edges = ()

    # extract the edge with highest edge betweenness centrality score and come out of the loop
    for key, value in sorted(graph_dictionary.items(), key=lambda item: item[1], reverse=True):
        set_of_edges = key
        break

    return set_of_edges


# This function uses the "edge_to_be_removed" function to determine the communities in the given graph
def girvan_newman(input_graph):
    # a generator over all connected components in the given graph
    generator_for_graph = nx.connected_components(input_graph)
    # find number of connected components
    generator_for_graph_count = nx.number_connected_components(input_graph)

    # as long as our graph is a single connected component
    while generator_for_graph_count == 1:
        # remove the edge with the highest EBC
        input_graph.remove_edge(edge_to_be_removed(input_graph)[0], edge_to_be_removed(input_graph)[1])
        # after removing the edge, find the number of connected components
        generator_for_graph = nx.connected_components(input_graph)
        generator_for_graph_count = nx.number_connected_components(input_graph)

    return generator_for_graph


# find communities in the graph
# pass a copy of the original graph since we will be removing the edges from the graph one by one
communities = girvan_newman(our_graph.copy())

# find the nodes which are forming the communities
group_of_nodes = []

for c in communities:
    group_of_nodes.append(list(c))
print(group_of_nodes)

# plot the communities and color the nodes of the communities
color_map = []
for node in our_graph:
    if node in group_of_nodes[0]:
        color_map.append('green')
    else:
        color_map.append('blue')

nx.draw(our_graph, node_color=color_map, with_labels=True)
plt.show()


