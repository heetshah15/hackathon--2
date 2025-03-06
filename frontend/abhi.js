import React, { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

const CLIENT_ID = "your_spotify_client_id";
const REDIRECT_URI = "your_redirect_uri";
const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize";
const RESPONSE_TYPE = "token";
const SCOPES = "user-top-read";

export default function SpotifyMovieRecommender() {
  const [token, setToken] = useState("");
  const [songs, setSongs] = useState([]);
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const hash = window.location.hash;
    let storedToken = window.localStorage.getItem("token");
    if (!storedToken && hash) {
      const newToken = new URLSearchParams(hash.substring(1)).get("access_token");
      if (newToken) {
        setToken(newToken);
        window.localStorage.setItem("token", newToken);
      }
    } else if (storedToken) {
      setToken(storedToken);
    }
  }, []);

  const getTopSongs = async () => {
    if (!token) return;
    const response = await fetch("https://api.spotify.com/v1/me/top/tracks?limit=5", {
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = await response.json();
    setSongs(data.items || []);
    fetchMovieRecommendations(data.items);
  };

  const fetchMovieRecommendations = async (songs) => {
    // Placeholder function to fetch movies based on songs
    const movieData = songs.map((song, index) => ({
      title: `Movie ${index + 1} based on ${song.name}`,
    }));
    setMovies(movieData);
  };

  const loginToSpotify = () => {
    window.location.href = `${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}&scope=${SCOPES}`;
  };

  return (
    <div className="flex flex-col items-center bg-black min-h-screen text-green-400 p-6">
      <h1 className="text-3xl font-bold mb-4">Spotify Movie Recommender</h1>
      {!token ? (
        <Button onClick={loginToSpotify} className="bg-green-500 hover:bg-green-600">
          Login with Spotify
        </Button>
      ) : (
        <Button onClick={getTopSongs} className="bg-green-500 hover:bg-green-600">
          Get Movie Recommendations
        </Button>
      )}
      <div className="mt-6 w-full max-w-lg">
        {movies.length > 0 && (
          <>
            <h2 className="text-xl font-semibold mb-2">Recommended Movies:</h2>
            {movies.map((movie, index) => (
              <motion.div key={index} initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
                <Card className="bg-gray-800 text-white mb-2 p-4">
                  <CardContent>{movie.title}</CardContent>
                </Card>
              </motion.div>
            ))}
          </>
        )}
      </div>
    </div>
  );
}