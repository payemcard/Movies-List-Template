import json

def load_movies():
    with open("db.json", "r") as file:
        return json.load(file)

def save_movies(movies):
    pass
