import sys
import requests
import pandas as pd
import networkx as nx
import numpy as np

def readEdgeList(filename):
	edgeList = pd.read_csv(filename)
	df = pd.DataFrame(edgeList)
	if len(df.columns) > 2:
		print "Warning: more than two columns. Returning only first two"
		df = df[df.columns[0:2]]
	return df

#print readEdgeList("testcsv.csv")

def degree(edgeList, in_or_out):
	df = readEdgeList(edgeList)
	if in_or_out == "in":
		degree_nodes = df['artistID_2'].value_counts()
	elif in_or_out == "out":
		degree_nodes = df['artistID'].value_counts()
	else:
		print "Error"
	return degree_nodes

#print degree('testcsv.csv', 'in')

def combineEdgelists(edgeList1, edgeList2):
	df1 = readEdgeList(edgeList1)
	df2 = readEdgeList(edgeList2)
	combinedLists = df1.append(df2)
	combinedLists = combinedLists.drop_duplicates()
	return combinedLists

#print combineEdgelists("testcsv.csv", "testcsv.csv")

def pandasToNetworkX(edgeList):
	graph = nx.DiGraph()
	df = readEdgeList(edgeList)
	edges = df.to_records(index=False)
	graph.add_edges_from(edges)
	#print graph.edges()
	return graph

#print pandasToNetworkX('testcsv.csv')

def randomCentralNode(inputDiGraph):
	edict = nx.eigenvector_centrality(inputDiGraph)
	normal = sum(edict.values())
	for k in edict:
		edict[k] = edict[k]/float(normal)
	randomNode= np.random.choice(edict.keys(), p = edict.values())
	return randomNode

#print randomCentralNode(pandasToNetworkX('testcsv.csv'))