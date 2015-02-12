from io import open
import csv
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo

def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY"""
    outFile = open('artists.csv', 'w', encoding='utf-8')
    try:
        outFile.write(u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY\n')
        for line in artist_info_list:
            ARTIST_ID = line['id']
            ARTIST_NAME = line['name']
            ARTIST_FOLLOWERS = line['followers']
            ARTIST_POPULARITY = line['popularity']
            outFile.write(u'%s,"%s",%s,%s\n' % (ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY))
    finally:
        outFile.close()

#artist_info_list = [{'id': '6vWDO969PvNqNYHIOW5v0m', 'name': u'Beyonc\xe9', 'followers': 2567234, 'popularity': 95 }]
#artist_info_list = fetchArtistInfo(fetchArtistId('Beyonce')) #using past functions
#writeArtistsTable(artist_info_list)

def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
    """
    outFile2 = open('albums.csv', 'w', encoding='utf-8')
    try:
        outFile2.write(u'ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n')
        for line in album_info_list:
            ARTIST_ID = line['artist_id']
            ALBUM_ID = line['album_id']
            ALBUM_NAME = line['name']
            ALBUM_YEAR = line['year']
            ALBUM_POPULARITY = line['popularity']
            outFile2.write(u'%s,%s,"%s",%s,%s\n' % (ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY))
    finally:
        outFile2.close()

#album_info_list = [{'artist_id': '6vWDO969PvNqNYHIOW5v0m','album_id': '2UJwKSBUz6rtW4QLK74kQu', 'name': u'BEYONC\xc9 [Platinum Edition]', 'year': u'2014','popularity': '92' }]

#writeAlbumsTable(album_info_list)
