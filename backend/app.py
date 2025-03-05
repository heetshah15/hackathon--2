from flask import Flask, request, jsonify
from spotify import get_song_metadata
from openai_helper import get_movie_recommendations

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    song_query = data.get('song_query')  # Could be a song, artist, or genre
    if not song_query:
        return jsonify({'error': 'No song query provided'}), 400

    # Fetch song metadata from Spotify
    try:
        metadata = get_song_metadata(song_query)
    except Exception as e:
        return jsonify({'error': f'Error fetching metadata: {str(e)}'}), 500

    # Use OpenAI to generate movie recommendations
    try:
        recommendations = get_movie_recommendations(metadata)
    except Exception as e:
        return jsonify({'error': f'Error getting movie recommendations: {str(e)}'}), 500

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)