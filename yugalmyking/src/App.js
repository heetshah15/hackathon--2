import React, { useState } from 'react';
import './App.css';
import logo2 from './logo2.png';

function App() {
  const [song, setSong] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const handleSearch = () => {
    // Placeholder for actual recommendation logic
    setRecommendations(['Movie 1', 'Movie 2', 'Movie 3']);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo2} alt="MUSICMATCH Logo" className="header-logo" />
        <h1>Song to Movie Recommendations</h1>
        <input
          type="text"
          placeholder="Enter your favorite song"
          value={song}
          onChange={(e) => setSong(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
        <div className="recommendations">
          {recommendations.length > 0 && (
            <ul>
              {recommendations.map((movie, index) => (
                <li key={index}>{movie}</li>
              ))}
            </ul>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;
