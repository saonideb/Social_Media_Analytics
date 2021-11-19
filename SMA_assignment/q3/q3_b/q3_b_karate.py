

!pip install igraph

import igraph

#the graph is read in gml format
g = igraph.read("karate.gml")

#We have calculated the edgelist here
edges = g.get_edgelist()

!pip install networkx
import networkx as nx

#Here the gml file is converted into a graph with the specified edges
G = nx.Graph(edges) 
print(G)

import matplotlib.pyplot as plt

# %matplotlib inline

# visualize the graph
nx.draw(G, with_labels = True)

#algorithm for Modularity Maximisation hereby
import networkx as nx
nx.__version__

#the details of the graph are viewed 
print(nx.info(G))
#print(G)

from networkx.algorithms.community import greedy_modularity_communities
import networkx.algorithms.community as nx_comm

#this function uses modularity maximization
c = list(greedy_modularity_communities(G))
#sorted(c)
#the number of the clusters are found out
length =len(c)
i=0
#the clusters are displayed here
while i<length:
  print(sorted(c[i]))
  i=i+1

nx_comm.modularity(G,nx_comm.label_propagation_communities(G))
print('Modularity of such partition for karate is %.3f' %(nx_comm.modularity(G,nx_comm.label_propagation_communities(G))))