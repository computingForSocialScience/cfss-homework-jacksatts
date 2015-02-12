import requests
from datetime import datetime

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/albums?album_type=album&market=US'
    req = requests.get(url)
    assert req.ok, 'n/a'
    data = req.json()
    assert data.get('items'), 'n/a'
    return [aID['id'] for aID in data['items']]

#print fetchAlbumIds('6vWDO969PvNqNYHIOW5v0m')

def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    url = 'https://api.spotify.com/v1/albums/' + album_id
    req = requests.get(url)
    assert req.ok, "n/a"
    data = req.json()
    AlbumInfo = {}
    assert data.get('name'), "n/a"
    AlbumInfo['artist_id'] = data['artists'][0]['id']
    AlbumInfo['album_id'] = album_id
    AlbumInfo['name'] = data['name']
    AlbumInfo['year'] = data['release_date'][:4]
    AlbumInfo['popularity'] = data['popularity']
    return AlbumInfo

#print fetchAlbumInfo('2UJwKSBUz6rtW4QLK74kQu')

