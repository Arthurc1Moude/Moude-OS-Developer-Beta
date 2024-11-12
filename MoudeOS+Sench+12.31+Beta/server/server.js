const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.static('public'));

app.get('/api/apps.json', (req, res) => {
  res.sendFile(__dirname + '/api/apps.json');
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
