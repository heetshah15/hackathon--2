import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_movie_recommendations(metadata):
    # Construct a prompt using the song's metadata
    prompt = f"""
Given the following song metadata from Spotify:
Song: {metadata['name']}
Artist: {metadata['artist']}
Album: {metadata['album']}
Audio Features: {metadata['audio_features']}

Recommend 3 movies that match the mood, energy, and themes of this song.
For each movie, provide a short explanation of why it fits.
"""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    text = response.choices[0].text.strip()
    return text
