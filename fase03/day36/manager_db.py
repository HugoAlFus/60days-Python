import sqlite3


def get_db_connection():
    conn = sqlite3.connect("tareas.db")
    conn.row_factory = sqlite3.Row  # Para acceder a columnas por nombre
    return conn


def create_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            completada INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()
    print("Base de datos creada correctamente.")


def add_task(task):
    conn = get_db_connection()
    conn.execute("INSERT INTO tareas (contenido) VALUES (?)", (task,))
    conn.commit()
    conn.close()


def get_all_task():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tareas").fetchall()
    conn.close()
    return tasks


def complete_task(id):
    conn = get_db_connection()
    task = conn.execute("SELECT completada FROM tareas WHERE id = ?", (id,)).fetchone()

    if task:
        new_state = 0 if task["completada"] else 1
        conn.execute("UPDATE tareas SET completada = ? WHERE id = ?", (new_state, id))
        conn.commit()
    conn.close()


def delete_task(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
