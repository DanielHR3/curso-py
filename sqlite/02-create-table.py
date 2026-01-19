import sqlite3

con = sqlite3.connect("sqlite/app.db")
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER primary key, nombre VARCHAR(50));
    """
)
con.commit() # sin este metodo no se guardan los cambios de tabla
con.close()
