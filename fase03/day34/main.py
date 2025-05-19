import csv
from collections import Counter

from flask import Flask, render_template, request
from matplotlib import pyplot as plt

app = Flask(__name__)
CSV_FILE = "votos.csv"


@app.route('/encuesta')
def form():
    return render_template("encuesta.html")


@app.route("/votar", methods=["POST"])
def vote():
    option = request.form.get("lenguaje")

    with open(CSV_FILE, mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([option])

    return f"Gracias por votar por {option} 😊"


@app.route("/estadisticas")
def stats():
    votes = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                votes.append(row[0])

    count = Counter(votes)
    generate_graph(count)
    return render_template("estadisticas.html")


def generate_graph(conteo):
    labels = list(conteo.keys())
    value = list(conteo.values())

    plt.figure(figsize=(8, 5))
    plt.bar(labels, value, color='skyblue')
    plt.title("Votos por lenguaje")
    plt.xlabel("Lenguajes")
    plt.ylabel("Cantidad de votos")
    plt.tight_layout()

    plt.savefig("static/votos.png")
    plt.close()


if __name__ == "__main__":
    app.run(debug=True)
