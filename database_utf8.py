import sqlite3

def connect():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT)")
    conn.commit()
    conn.close()

def insert(name, phone, email, address):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO contact VALUES (NULL, ?, ?, ?, ?)", (name, phone, email, address))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="", phone="", email="", address=""):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact WHERE name=? OR phone=? OR email=? OR address=?", (name, phone, email, address))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contact WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, phone, email, address):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("UPDATE contact SET name=?, phone=?, email=?, address=? WHERE id=?", (name, phone, email, address, id))
    conn.commit()
    conn.close()

connect()
