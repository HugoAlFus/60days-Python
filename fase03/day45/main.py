from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/contacto', methods=["POST"])
def contact():
    name = request.form["nombre"]
    email = request.form["email"]
    message = request.form["mensaje"]
    print(f"Mensaje recibido de {name} ({email}): {message}")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
