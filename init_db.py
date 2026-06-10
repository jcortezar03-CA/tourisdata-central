import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    contrasena TEXT NOT NULL
)
''')

cursor.execute("DELETE FROM Usuarios")
cursor.execute("INSERT INTO Usuarios (usuario, contrasena) VALUES (?, ?)", ('tourisadmin', 'TuriSafe2026!'))

conn.commit()
conn.close()

print("Base de datos creada en", DB_PATH)
