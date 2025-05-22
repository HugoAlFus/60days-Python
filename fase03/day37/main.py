import json
import os.path

import markdown
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
FILE = "notas_guardadas.json"


def upload_notes():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding='utf-8') as f:
        return json.load(f)


def save_notes(notes):
    with open(FILE, "w", encoding='utf-8') as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)


def get_note_by_id(note_id):
    with open(FILE, 'r', encoding='utf-8') as f:
        notes = json.load(f)
        for note in notes:
            if note.get("id") == note_id:
                return note
    return None


@app.route('/')
def home():
    notes = upload_notes()
    return render_template("index.html", notas=notes)


@app.route('/guardar', methods=["POST"])
def save():
    notes = upload_notes()
    content = request.form.get("contenido")
    new_note = {
        'id': len(notes) + 1,
        'titulo': request.form.get("titulo"),
        'contenido': content,
        'contenido_html': markdown.markdown(content)
    }
    notes.append(new_note)
    save_notes(notes)
    return redirect("/")


@app.route('/ver/<int:id>', )
def see_note(id):
    note = get_note_by_id(id)
    return render_template("ver_nota.html", nota=note)


if __name__ == "__main__":
    app.run(debug=True)
