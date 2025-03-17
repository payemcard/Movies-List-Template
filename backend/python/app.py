from flask import Flask, jsonify, request
from flask_cors import CORS

from db_utils import load_movies, update_movie

app = Flask(__name__)
CORS(app)

@app.route("/api/movies", methods=["GET"])
def get_movies():
    pass

@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)