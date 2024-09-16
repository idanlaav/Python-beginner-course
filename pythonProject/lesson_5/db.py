import sqlite3

conn = sqlite3.connect('mydatabase.db')

def create_user(username, password):
    try:
        sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"Error creating user: {e}")
        return 0
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    if cur.fetchone() == None:
        return False
    else:
        return True

def login(username, password):
    try:
        sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cur = conn.cursor()
        cur.execute(sql)
        if cur.fetchone() is None:
            return False
        else:
            return True
    except Exception as e:
        print(f"Error logging in: {e}")
        return False
