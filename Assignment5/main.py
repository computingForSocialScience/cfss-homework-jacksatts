import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "input artists are ", artist_names
    # YOUR CODE HERE
    artist_list = []
    album_list = []
    for x in artist_names: 	
    	artist_id = fetchArtistId(x)
    	artist_info = fetchArtistInfo(artist_id)
        artist_list.append(artist_info)
        album_id = fetchAlbumIds(artist_id)
        albums_info = [fetchAlbumInfo(y) for y in album_id]
        album_list +=albums_info

    writeArtistsTable(artist_list)
    writeAlbumsTable(album_list)
    plotBarChart()


