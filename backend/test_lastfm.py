from lastfm import get_song_metadata

def main():
    song_query = input("Enter a song query to test Last.fm integration: ")
    try:
        metadata = get_song_metadata(song_query)
        print("Metadata retrieved:")
        print(metadata)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
