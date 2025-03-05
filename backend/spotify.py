import requests # imports
import base64
import os
import time
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

access_token = None # storing token and expires time
access_token_expires = 0

def get_spotify_token():
    global access_token, access_token_expires
    if access_token and time.time() < access_token_expires:
        return access_token
    
    auth_str = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    headers = {
        "Authorization": f"Basic {b64_auth_str}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    if response.status_code != 200:
        raise Exception("Failed to authenticate with Spotify API")
    token_info = response.json()
    access_token = token_info['access_token']
    token_expires = time.time() + token_info['expires_in'] - 10  # Buffer time before expiry
    return access_token

def get_song_metadata(song_query):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    # Search for the song using the provided query
    params = {
        "q": song_query,
        "type": "track",
        "limit": 1
    }
    search_url = "https://api.spotify.com/v1/search"
    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch song data from Spotify")
    results = response.json()
    tracks = results.get("tracks", {}).get("items", [])
    if not tracks:
        raise Exception("No track found for the query")
    track = tracks[0]
    track_id = track['id']

    # Retrieve audio features for the track
    audio_features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    features_response = requests.get(audio_features_url, headers=headers)
    if features_response.status_code != 200:
        raise Exception("Failed to fetch audio features from Spotify")
    audio_features = features_response.json()

    # Combine relevant metadata
    metadata = {
        "name": track["name"],
        "artist": track["artists"][0]["name"],
        "album": track["album"]["name"],
        "audio_features": audio_features,
        "preview_url": track.get("preview_url")
    }
    return metadata