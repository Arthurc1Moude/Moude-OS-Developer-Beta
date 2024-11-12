import React, { useEffect, useState } from 'react';

const VoiceAssistant = () => {
  const [transcript, setTranscript] = useState('');

  useEffect(() => {
    const recognition = new window.SpeechRecognition();
    recognition.continuous = true;
    recognition.lang = 'en-US';

    recognition.onresult = (event) => {
      const speechToText = event.results[event.resultIndex][0].transcript;
      setTranscript(speechToText);
    };

    recognition.start();

    return () => recognition.stop();
  }, []);

  return (
    <div className="voice-assistant">
      <p>{transcript}</p>
    </div>
  );
};

export default VoiceAssistant;
