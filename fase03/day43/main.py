import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")


@app.route('/')
def home():
    return render_template("movies.html")


@app.route('/api/search')
def search_movies():
    title = request.args.get('title', '')
    if not title:
        return jsonify({"error": "Falta el parámetro 'title'"}), 400

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={title}&type=movie"
    response = requests.get(url)
    return jsonify(response.json())


@app.route('/api/details')
def movie_details():
    movie_id = request.args.get('id', '')
    if not movie_id:
        return jsonify({"error": "Falta el parámetro 'id'"}), 400

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={movie_id}&plot=full&type=movie"
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)