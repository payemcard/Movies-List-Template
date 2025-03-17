from flask import Flask, jsonify, request
from flask_cors import CORS

from db_utils import load_movies, add_movie, update_movie

app = Flask(__name__)
CORS(app)

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(load_movies())

@app.route("/api/movies", methods=["POST"])
def create_movie():
    movie = request.json
    new_movie = add_movie(movie)
    return jsonify(new_movie), 201

@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie_endpoint(movie_id):
    updated_data = request.json
    updated_movie = update_movie(movie_id, updated_data)
    if updated_movie:
        return jsonify(updated_movie)
    return jsonify({"error": "Movie not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)