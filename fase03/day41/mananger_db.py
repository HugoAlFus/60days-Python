import sqlite3


def get_db_connection():
    conn = sqlite3.connect("entradas.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS entradas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        contenido text not null
    )
''')

    conn.commit()
    conn.close()
    print("Base de datos creada correctamente.")


def add_entry(title, content):
    conn = get_db_connection()
    conn.execute("INSERT INTO entradas (titulo, contenido) VALUES (?,?)", (title, content))
    conn.commit()
    conn.close()


def get_all_entries():
    conn = get_db_connection()
    entries = conn.execute("SELECT * FROM entradas").fetchall()
    conn.close()
    return entries


def get_entry_by_id(id):
    conn = get_db_connection()
    entry = conn.execute("SELECT * FROM entradas where id = ?", (id,)).fetchone()
    conn.close()
    return entry


def delete_entry(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM entradas WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def edit_entry(id, title, content):
    conn = get_db_connection()
    conn.execute("UPDATE entradas SET titulo = ?, contenido = ? where id = ?", (title, content, id))
    conn.commit()
    conn.close()
