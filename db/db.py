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
            CREATE TABLE IF NOT EXISTS chat (
                user_id TEXT,
                chat_id TEXT UNIQUE,
                chat_time TEXT,
                chat_name TEXT,
                chat_len BIGINT,
                chat_data TEXT,
                chat_analysis TEXT,
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

def add_chat(user_id, chat_id, chat_time, chat_name, chat_len, chat_data, result):
    mutate("INSERT INTO chat VALUES (?, ?, ?, ?, ?, ?, ?)", (user_id, chat_id, chat_time, chat_name, chat_len, chat_data, result))

def delete_chat(user_id, chat_id):
    mutate("DELETE FROM chat WHERE user_id = ? AND chat_id = ?", (user_id, chat_id))

def get_chats(user_id):
    return query("SELECT * FROM chat WHERE user_id = ?", (user_id, ))

def get_chat_by_id(user_id, chat_id):
    return query("SELECT * FROM chat WHERE user_id = ? AND chat_id = ?", (user_id, chat_id))

def get_chat_by_name(user_id, chat_name):
    return query("SELECT * FROM chat WHERE user_id = ? AND chat_name = ?", (user_id, chat_name))