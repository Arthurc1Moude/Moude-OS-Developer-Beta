import React from 'react';
import Dock from './components/Dock';
import VoiceAssistant from './components/VoiceAssistant';
import WallpaperManager from './components/WallpaperManager';
import MoudeStore from './components/MoudeStore';
import SenchCode from './components/SenchCode';
import ZodobStudio from './components/ZodobStudio';

const App = () => {
  return (
    <div>
      <WallpaperManager />
      <Dock />
      <VoiceAssistant />
      <MoudeStore />
      <SenchCode />
      <ZodobStudio />
    </div>
  );
};

export default App;
