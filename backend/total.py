from gemini_api_helper import get_movie_recommendations
from lastfm import get_song_metadata

def main():
    # Prompt the user for a song query.
    song_query = input("Enter a song query: ")

    try:
        # Fetch song metadata from Last.fm based on user input.
        metadata = get_song_metadata(song_query)
        print("Song Metadata:")
        print(metadata)
        
        # Generate movie recommendations using Gemini based on the fetched metadata.
        recommendations = get_movie_recommendations(metadata)
        print("Movie Recommendations:")
        print(recommendations)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
