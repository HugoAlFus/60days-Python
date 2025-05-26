from flask import Flask, render_template, request, redirect, session, url_for

import mananger_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreto-super-seguro'
USER = "Admin"
PASSWORD = "1234"


@app.route('/')
def home():
    entrys = mananger_db.get_all_entries()
    return render_template("blog.html", entradas=entrys)


@app.route('/login', methods=["POST"])
def login():
    user = request.form['username']
    password = request.form['password']

    if user == USER and PASSWORD == password:
        session['logged_in'] = True
        return redirect(url_for('home'))
    else:
        return "Credenciales incorrectas", 401


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/add', methods=["POST"])
def add_entry():
    if not session.get('logged_in'):
        return "No autorizado", 403
    title = request.form['titulo']
    content = request.form['contenido']
    mananger_db.add_entry(title, content)
    return redirect(url_for('home'))


@app.route('/delete/<int:id>', methods=["POST"])
def delete_entry(id):
    if not session.get('logged_in'):
        return "No autorizado", 403
    mananger_db.delete_entry(id)
    return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_entry(id):
    if not session.get('logged_in'):
        return "No autorizado", 403
    entry = mananger_db.get_entry_by_id(id)
    if request.method == 'POST':
        title = request.form['titulo']
        content = request.form['contenido']
        mananger_db.edit_entry(id, title, content)
        return redirect(url_for('home'))

        # Si GET, renderizar formulario de edición
    return render_template('edit.html', entrada=entry)


if __name__ == "__main__":
    mananger_db.create_db()
    app.run(debug=True)
