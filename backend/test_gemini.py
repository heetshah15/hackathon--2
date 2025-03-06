from gemini_api_helper import get_movie_recommendations

def main():
    # dummy metadata for testing
    metadata = {
        "name": "Shape of You",
        "artist": "Ed Sheeran",
        "album": "Divide",
        "tags": ["pop", "upbeat", "romantic"],
        "wiki": "A hit song by Ed Sheeran that is upbeat and catchy."
    }
    try:
        recommendations = get_movie_recommendations(metadata)
        print("Movie Recommendations:")
        print(recommendations)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
