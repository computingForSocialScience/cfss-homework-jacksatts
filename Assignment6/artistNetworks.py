import sys
import requests
import pandas as pd

def getRelatedArtists(artistID):
	"""Returns a list of related artists"""
	url = "https://api.spotify.com/v1/artists/" + artistID + "/related-artists"
	req = requests.get(url)
	assert req.ok, 'n/a'
	data = req.json()
	assert data.get('artists'), 'n/a'
	return [aID['id'] for aID in data['artists']]

#print getRelatedArtists('2mAFHYBasVVtMekMUkRO9g')

def getDepthEdges(artistID, depth):
	artist_tree = []
	searchList = getRelatedArtists(artistID)

	for a in searchList:
		tup = artistID, a
		artist_tree.append(tup)

	while depth > 0:
		for id in searchList:
			temp_list = getRelatedArtists(id)
			for x in temp_list:
				tup = id, x
				if tup in artist_tree:
					pass
				else:
					artist_tree.append(tup)
		depth = depth -1		
		searchList = temp_list

	return artist_tree

#print getDepthEdges('2mAFHYBasVVtMekMUkRO9g', 2)
#print len(getDepthEdges('2mAFHYBasVVtMekMUkRO9g', 2))

def getEdgeList(artistID, depth):
	tuple_list = getDepthEdges(artistID, depth)
	edge_list = pd.DataFrame(tuple_list)
	edge_list.columns = ["artistID", "artistID_2"]
	return edge_list

#print getEdgeList('2mAFHYBasVVtMekMUkRO9g', 1)

def writeEdgeList(artistID, depth, filename):
	save_edge_list = getEdgeList(artistID, depth)
	save_csv_file = save_edge_list.to_csv(filename, index = False)

#writeEdgeList('2mAFHYBasVVtMekMUkRO9g', 1, 'testcsv.csv')