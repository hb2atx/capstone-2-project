import React, { useState, useEffect } from 'react';
import OverPaidApi from './api/api';

function AllPlayerStats() {
  const [allPlayerStats, setAllPlayerStats] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        // Fetch all player stats
        const playerStats = await OverPaidApi.getAllPlayerStats();
        setAllPlayerStats(playerStats);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching all player stats:', error);
        setError('Error fetching all player stats. Please try again later.');
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  // Render your component using allPlayerStats
  return (
    <div>
      <h1>All Player Stats</h1>
      <ul>
        {allPlayerStats.map((player) => (
          <li key={player.id}>
            {player.name} - {player.position} - {player.stats}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AllPlayerStats;
