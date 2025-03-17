const fs = require('fs');
const dbPath = './db.json';

function loadMovies() {
    return JSON.parse(fs.readFileSync(dbPath));
}

function saveMovies(movies) {
    fs.writeFileSync(dbPath, JSON.stringify(movies, null, 4));
}

function addMovie(movie) {
    const movies = loadMovies();
    movie.id = Math.max(...movies.map(m => m.id)) + 1;
    movies.push(movie);
    saveMovies(movies);
    return movie;
}

function updateMovie(movieId, updatedData) {
    let movies = loadMovies();
    let movie = movies.find(m => m.id === movieId);
    if (movie) {
        Object.assign(movie, updatedData);
        saveMovies(movies);
        return movie;
    }
    return null;
}

module.exports = { loadMovies, addMovie, updateMovie };