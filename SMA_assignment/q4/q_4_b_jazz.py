# -*- coding: utf-8 -*-
"""q_4_b_jazz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kGjQsAC-sVcB-mhrql7ZutBpqpFudI3A
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
#%cd /content/drive/MyDrive/SMA_A1/
# %cd /content/drive/MyDrive/Semester_3/SMA/

!pip install igraph

import igraph

g = igraph.read("jazz.net",format="pajek")

A = g.get_edgelist()

!pip install networkx
import networkx as nx

G = nx.Graph(A) 
print(G)

# Commented out IPython magic to ensure Python compatibility.
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
from datetime import datetime
start=datetime.now()
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
print('Modularity of such partition for Jazz is %.3f' %(nx_comm.modularity(G,nx_comm.label_propagation_communities(G))))
print(datetime.now()-start)

import statistics
set = [0.278250, 0.337633, 0.283783,0.292721, 0.288915]
print(statistics.mean(set))