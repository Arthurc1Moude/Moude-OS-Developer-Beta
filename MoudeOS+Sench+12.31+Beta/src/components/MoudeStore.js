import React, { useEffect, useState } from 'react';

const MoudeStore = () => {
  const [apps, setApps] = useState([]);

  useEffect(() => {
    fetch('/api/apps.json')
      .then((response) => response.json())
      .then((data) => setApps(data))
      .catch((error) => console.error('Error fetching apps:', error));
  }, []);

  return (
    <div className="moude-store">
      <h2>Moude Store</h2>
      <ul>
        {apps.map((app, index) => (
          <li key={index}>
            <h3>{app.name}</h3>
            <p>{app.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MoudeStore;
