import requests
from config import GEMINI_API_KEY

# Hypothetical Gemini EPI endpoint – update with the actual endpoint if different.
GEMINI_API_ENDPOINT = "https://generativelanguage.googleapis.com/v1/complete"

def get_movie_recommendations(metadata):
    # Construct a prompt using the track metadata.
    prompt = f"""
Given the following track details:
Song: {metadata.get('name')}
Artist: {metadata.get('artist')}
Album: {metadata.get('album')}
Tags: {', '.join(metadata.get('tags', []))}
Wiki Summary: {metadata.get('wiki')}

Based on this information, recommend 3 movies that align with the mood, themes, and style of the song.
For each recommendation, provide a brief explanation of why it fits.
"""
    # Set up the payload.
    payload = {
        "prompt": prompt,
        "max_tokens": 250,
        "temperature": 0.7,
        "n": 1,
    }
    
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(GEMINI_API_ENDPOINT, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error from Gemini API: {response.status_code}, {response.text}")
    
    data = response.json()
    recommendation_text = data.get("choices", [{}])[0].get("text", "").strip()
    return recommendation_text
