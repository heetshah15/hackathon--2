import requests
from config import LASTFM_API_KEY

BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def search_track(track_query):
    """Search for a track using the Last.fm track.search method."""
    params = {
        "method": "track.search",
        "track": track_query,
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "limit": 1
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"Error searching for track: {response.status_code}, {response.text}")
    
    data = response.json()
    trackmatches = data.get("results", {}).get("trackmatches", {}).get("track", [])
    if not trackmatches:
        raise Exception("No track found for the query")
    
    return trackmatches[0]

def get_track_info(artist, track):
    """Fetch detailed track info using the Last.fm track.getInfo method."""
    params = {
        "method": "track.getInfo",
        "artist": artist,
        "track": track,
        "api_key": LASTFM_API_KEY,
        "format": "json"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching track info: {response.status_code}, {response.text}")
    
    data = response.json()
    if "track" not in data:
        raise Exception("Track info not found")
    
    return data["track"]

def get_song_metadata(song_query):
    """
    Searches for a track using Last.fm and returns detailed metadata including:
      - Track name
      - Artist
      - Album (if available)
      - Tags (as a list)
      - Wiki summary (if available)
    """
    basic_track = search_track(song_query)
    track_name = basic_track.get("name")
    artist_name = basic_track.get("artist")
    
    # Fetch detailed track info
    track_info = get_track_info(artist_name, track_name)
    
    # Album details (if available)
    album = None
    if "album" in track_info and track_info["album"]:
        album = track_info["album"].get("title")
    
    # Gather tags
    tags = []
    if "toptags" in track_info and "tag" in track_info["toptags"]:
        for tag in track_info["toptags"]["tag"]:
            tags.append(tag.get("name"))
    
    # Wiki summary (if available)
    wiki = None
    if "wiki" in track_info:
        wiki = track_info["wiki"].get("summary")
    
    metadata = {
        "name": track_name,
        "artist": artist_name,
        "album": album,
        "tags": tags,
        "wiki": wiki
    }
    return metadata
