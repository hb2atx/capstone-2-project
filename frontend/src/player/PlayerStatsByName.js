// Import necessary modules
import React, { useEffect, useState } from 'react';
import OverPaidApi from '../api/api';

function PlayerStatsByName({ match }) {
  const [playerStats, setPlayerStats] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Extract player name from the URL parameter
  const playerName = match.params.name;

  useEffect(() => {
    async function fetchData() {
      try {
        // Fetch player stats by name
        const playerStatsData = await OverPaidApi.getPlayerStatsByName(playerName);
        setPlayerStats(playerStatsData);
        setLoading(false);
      } catch (error) {
        console.error(`Error fetching player stats for ${playerName}:`, error);
        setError(`Error fetching player stats for ${playerName}. Please try again later.`);
        setLoading(false);
      }
    }

    fetchData();
  }, [playerName]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  // Render your component using playerStats
  return (
    <div>
      <h1>Player Stats for {playerName}</h1>
      <ul>
        <li>
          {playerStats.name} - {playerStats.position} - {playerStats.stats}
        </li>
      </ul>
    </div>
  );
}

export default PlayerStatsByName;
