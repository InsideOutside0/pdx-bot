import sqlite3 as sql
from pathlib import Path
import config

con = sql.connect('database.db')
c = con.cursor()


def create_db():
    print("Failed to locating 'database.db.' Generating new file")
    Path("database.db").touch()


def create_server_table(s):
    c.execute('''CREATE TABLE %s (username text, troops integer)''', s)
