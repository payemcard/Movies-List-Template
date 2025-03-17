import json

def load_movies():
    with open("db.json", "r") as file:
        return json.load(file)

def save_movies(movies):
    with open("db.json", "w") as file:
        json.dump(movies, file, indent=4)

def update_movie(movie_id, updated_data):
    movies = load_movies()
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(updated_data)
            save_movies(movies)
            return movie
    return None