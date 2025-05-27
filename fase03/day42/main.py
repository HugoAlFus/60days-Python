import os

import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")


@app.route('/')
def home():
    return render_template("crypto_dashboard.html")


@app.route('/api/price/<crypto>')
def get_crypto_price(crypto):
    url = f"https://rest.coincap.io/v3/assets/{crypto}?apiKey={API_KEY}"

    try:
        response = requests.get(url)
        print("Respuesta cruda:", response.text)
        data = response.json()
        price = float(data["data"]["priceUsd"])
        return jsonify({"price": round(price, 2)})

    except Exception as e:
        print(str(e))
        return jsonify({"error": "No se pudo obtener el precio" + str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
