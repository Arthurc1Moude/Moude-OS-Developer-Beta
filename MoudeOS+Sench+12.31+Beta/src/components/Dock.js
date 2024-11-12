import React from 'react';

const Dock = () => {
  const apps = ['App1', 'App2', 'App3'];

  return (
    <div className="dock">
      {apps.map((app, index) => (
        <div key={index} className="dock-item">
          {app}
        </div>
      ))}
    </div>
  );
};

export default Dock;
