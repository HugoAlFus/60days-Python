import sqlite3


def get_db_connection():
    conn = sqlite3.connect("tweets.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contenido TEXT NOT NULL,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

    conn.commit()
    conn.close()
    print("Base de datos creada correctamente.")


def add_tweet(tweet):
    conn = get_db_connection()
    conn.execute("INSERT INTO tweets (contenido) VALUES (?)", (tweet,))
    conn.commit()
    conn.close()


def get_all_tweets():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tweets").fetchall()
    conn.close()
    return tasks

def delete_tweet(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tweets WHERE id = ?", (id,))
    conn.commit()
    conn.close()
