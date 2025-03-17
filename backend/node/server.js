const express = require('express');
const { loadMovies, updateMovie } = require('./dbUtils');

const app = express();
app.use(express.json());

app.get('/api/movies', (req, res) => {
    res.status(200).send("GET request received. Implement logic here.");
});

app.put('/api/movies/:id', (req, res) => {
    res.status(200).send("PUT request received. Implement logic here.");
});

app.listen(5000, () => console.log('Server running on port 5000'));