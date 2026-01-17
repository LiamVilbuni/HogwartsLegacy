import sqlite3

def create_connection():
    return sqlite3.connect("sortinghat.db")

def create_tables():
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                email TEXT UNIQUE,
                name TEXT,
                avatar TEXT
            );
            CREATE TABLE IF NOT EXISTS content (
                user_id TEXT,
                content_id TEXT UNIQUE,
                content_name TEXT,
                content_data TEXT,
                result TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)

def query(query, params=()):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute(query, params)
        return cur.fetchall()

def mutate(query, params=()):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute(query, params)
        cur.fetchall()
        conn.commit()

def add_content(user_id, content_id, content_name, content_data, result):
    mutate("INSERT INTO content VALUES (?, ?, ?, ?, ?)", (user_id, content_id, content_name, content_data, result))

def delete_content(user_id, content_id):
    mutate("DELETE FROM content WHERE user_id = ? AND content_id = ?", (user_id, content_id))

def get_content(user_id):
    return query("SELECT * FROM content WHERE user_id = ?", (user_id, ))

def get_content_by_id(user_id, content_id):
    return query("SELECT * FROM content WHERE user_id = ? AND content_id = ?", (user_id, content_id))

def get_content_by_name(user_id, content_name):
    return query("SELECT * FROM content WHERE user_id = ? AND content_name = ?", (user_id, content_name))