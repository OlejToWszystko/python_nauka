#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nauka_grafów.py

import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot
from numpy import array


def sort_edges_due_to_weight(edges):
	#sortowanie bąbelkowe
	flag = True
	n = len(edges)
	while flag == True:
		flag = False
		for i in range(n-1):
			if edges[i][-1]['weight'] > edges[i+1][-1]['weight']:
				edges[i], edges[i+1] = edges[i+1], edges[i]
				flag = True
		n -= 1
		
	print("Posortowane krawędzie : ")			
	print(edges)

	

H = nx.path_graph(10)

G = nx.Graph()
G.add_nodes_from(H)
G.add_edges_from(H.edges())

print(G.nodes(), G.number_of_nodes())
print(G.edges(), G.number_of_edges())
print(G[1])

edgelist = [('a','b',{'weight':4}), 
			('a','e',{'weight':1}),
			('a','f',{'weight':2}),
			('b','a',{'weight':4}),
			('b','e',{'weight':2}),
			('b','c',{'weight':2}),
			('c','b',{'weight':2}),
			('c','d',{'weight':8}),
			('d','c',{'weight':8}),
			('d','e',{'weight':3}),
			('d','f',{'weight':6}),
			('e','a',{'weight':1}),
			('e','b',{'weight':2}),
			('e','d',{'weight':3}),
			('e','f',{'weight':7}),
			('f','a',{'weight':2}),
			('f','d',{'weight':6}),
			('f','e',{'weight':7})]
			
graf = nx.Graph(edgelist)

print("Wierzchołki grafu : ", graf.nodes(), graf.number_of_nodes())
print("Krawędzie grafu : ", graf.edges(data='weight'), graf.number_of_edges())
print(nx.degree(graf))

sort_edges_due_to_weight(graf.edges(data=True))

T = nx.minimum_spanning_tree(graf)
print("Minimalne drzewo rozpinające")
print(T.edges(data=True))
print("Posortowane")
print(sorted([edge[::-1] for edge in T.edges(data='weight')]))
position = nx.circular_layout(graf)
labels = dict(((u, v), d) for u, v, d in graf.edges(data='weight'))
labelsT = dict(((u, v), d) for u, v, d in T.edges(data='weight'))
print(position)

#nx.draw(graf)
#nx.draw_networkx(graf)
fig1, (sp1, sp2) = plt.subplots(1, 2)
nx.draw_networkx(graf, pos=position, ax=sp1)
nx.draw_networkx_edge_labels(graf, pos=position, edge_labels=labels, ax=sp1)
nx.draw_networkx(T, pos=position, ax=sp2)
nx.draw_networkx_edge_labels(T, pos=position, edge_labels=labelsT, ax=sp2)
#nx.draw_networkx_edges(graf, pos=nx.spring_layout(graf))
#nx.draw_networkx_edge_labels(graf, pos=nx.spring_layout(graf))

fig1.tight_layout()
plt.show()
#nx.draw_graphviz(graf, prog='neato')
#write_dot(graf, 'graf.dot')
