import os
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template("filtros.html")


@app.route('/procesar', methods=["POST"])
def filter():
    img = request.files.get("imagen")
    filtre = request.form.get("filtro")

    path_original = os.path.join(app.config['UPLOAD_FOLDER'], "original.png")
    img.save(path_original)

    img = Image.open(path_original)

    if filtre == "grayscale":
        img = img.convert("L")
    elif filtre == "rotate":
        img = img.rotate(90)
    elif filtre == "resize":
        img = img.resize((img.width // 2, img.height // 2))

    path_processed = os.path.join(app.config['UPLOAD_FOLDER'], "procesada.png")
    img.save(path_processed)

    return render_template("filtros.html", imagen_url="procesada.png")


if __name__ == "__main__":
    app.run(debug=True)
