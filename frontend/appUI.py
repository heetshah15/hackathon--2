import streamlit as st
import requests

st.title("Movie Recommendations Based on Music Taste")

song_query = st.text_input("Enter a song, artist, or genre:")

if st.button("Get Recommendations"):
    if not song_query:
        st.error("Please enter a valid song query")
    else:
        # Call the backend API (ensure the Flask server is running at localhost:5000)
        try:
            response = requests.post("http://localhost:5000/recommend", json={"song_query": song_query})
            if response.status_code == 200:
                data = response.json()
                st.subheader("Movie Recommendations:")
                st.write(data["recommendations"])
            else:
                st.error("Error: " + response.text)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
