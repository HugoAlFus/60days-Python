from flask import Flask, render_template, request, redirect

from fase03.day36 import manager_db
from manager_db import create_db, complete_task, get_all_task, delete_task

app = Flask(__name__)


@app.route('/')
def home():
    tasks = get_all_task()
    print()
    return render_template("index.html", tareas=tasks)


@app.route('/add', methods=["POST"])
def add_task():
    new_task = request.form.get("tarea")
    manager_db.add_task(new_task)
    return redirect("/")


@app.route("/toggle/<int:id>", methods=["POST"])
def complete(id):
    complete_task(id)
    return redirect("/")


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    delete_task(id)
    return redirect("/")


if __name__ == "__main__":
    create_db()
    app.run(debug=True)
