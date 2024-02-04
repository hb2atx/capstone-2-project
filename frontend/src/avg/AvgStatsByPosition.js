// Import necessary dependencies
import React, { useEffect, useState } from 'react';
import OverPaidApi from '../api/api';

// DynamicAvgStats component
function AvgStatsByPosition({ match }) {
  const [avgStats, setAvgStats] = useState(null);
  const position = match.params.position;

  useEffect(() => {
    // Fetch average stats for the specified position
    async function fetchAvgStats() {
      try {
        const avgStats = await OverPaidApi.getAvgStatsByPosition(position);
        setAvgStats(avgStats);
      } catch (error) {
        console.error('Error fetching average stats:', error);
      }
    }

    fetchAvgStats();
  }, [position]);

  // Display loading message while fetching data
  if (!avgStats) {
    return <p>Loading...</p>;
  }

  // Display the fetched average stats
  return (
    <div>
      <h2>Average Stats for {position}</h2>
    </div>
  );
}

export default  AvgStatsByPosition;
