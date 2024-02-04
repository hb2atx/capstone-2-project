import React, { useEffect, useState } from 'react';
import OverPaidApi from "../api/api";

function AllAvgStats() {
  const [avgPlayerStats, setAvgPlayerStats] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        // Fetch average player stats at all positions
        const avgStats = await OverPaidApi.getAvgPlayerStats();
        setAvgPlayerStats(avgStats);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching average player stats:', error);
        setError('Error fetching average player stats. Please try again later.');
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

  // Render your component using avgPlayerStats
  return (
    <div>
      <h1>Average Player Stats at All Positions</h1>
      <ul>
        {Object.entries(avgPlayerStats).map(([position, stats]) => (
          <li key={position}>
            {position}: {stats}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AllAvgStats;

