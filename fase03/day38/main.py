import requests
from flask import Flask, render_template, request

app = Flask(__name__)

PATH_API = "https://www.googleapis.com/books/v1/volumes?q="


@app.route('/', methods=['GET'])
def home():
    query = request.args.get('query')
    books = []

    print(query)
    if query:
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            books = data.get('items', [])
            print(books)

    return render_template('index.html', books=books, query=query)


if __name__ == "__main__":
    app.run(debug=True)
