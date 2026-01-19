import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO usuario (nombre) VALUES (?)",
        ("Hola Mundo",),
    )
    con.commit()
