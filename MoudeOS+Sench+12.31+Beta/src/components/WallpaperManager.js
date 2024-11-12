import React, { useEffect } from 'react';

const WallpaperManager = () => {
  useEffect(() => {
    document.body.style.background = 'linear-gradient(135deg, #4a00e0, #8e2de2)';
  }, []);

  return null;
};

export default WallpaperManager;
