'''import requests
from config import GEMINI_API_KEY

GEMINI_API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyD_hSkU6mWd6ANn3utOpK7JBaKYb5wDah8"

def get_movie_recommendations(metadata):
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

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GEMINI_API_ENDPOINT, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error from Gemini API: {response.status_code}, {response.text}")

    data = response.json()

    recommendation_text = data.get("candidates", [{}])[0].get("content", {}).get("parts",[{}])[0].get("text","").strip()
    return recommendation_text
'''

from google import genai
from config import GEMINI_API_KEY

# Initialize the client with your Gemini API key.
client = genai.Client(api_key=GEMINI_API_KEY)

def get_movie_recommendations(metadata):
    """
    Uses Google Gemini to generate movie recommendations based on track metadata.
    
    Parameters:
      metadata (dict): Contains keys 'name', 'artist', 'album', 'tags', 'wiki'
      
    Returns:
      str: The generated movie recommendations text.
    """
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
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

