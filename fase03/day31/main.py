from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {"title": "Mi primer post", "date": "2025-05-14", "content": "¡Hola mundo desde mi mini blog!"},
        {"title": "Segundo post", "date": "2025-05-15", "content": "Hoy aprendí a usar Flask y plantillas HTML."}
    ]
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
