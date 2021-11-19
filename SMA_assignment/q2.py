import networkx
import numpy
import igraph

karate_graph = igraph.read("karate.gml")
dolphins_graph = igraph.read("dolphins.gml")
jazz_graph = igraph.read("jazz.net",format="pajek")

# number of nodes in the graphs read above
print("No of nodes in Karate dataset: ", karate_graph.vcount())
print("No of nodes in Dolphins dataset: ", dolphins_graph.vcount())
print("No of nodes in Jazz dataset: ", jazz_graph.vcount())

# number of edges in the graphs
print("No of edges in Karate dataset: ", karate_graph.ecount())
print("No of edges in Dolphins dataset: ", dolphins_graph.ecount())
print("No of edges in Jazz dataset: ", jazz_graph.ecount())

# average path lengths
print("Average Path Length in Karate dataset: ", karate_graph.average_path_length())
print("Average Path Length in Dolphins dataset: ", dolphins_graph.average_path_length())
print("Average Path Length in Jazz dataset: ", jazz_graph.average_path_length())

# average clustering coefficient
print("average clustering coefficient in Karate dataset: ", karate_graph.transitivity_undirected())
print("average clustering coefficient in Dolphins dataset: ", dolphins_graph.transitivity_undirected())
print("average clustering coefficient in Jazz dataset: ", jazz_graph.transitivity_undirected())

