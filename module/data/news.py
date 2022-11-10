import sqlite3

cur.execute("""CREATE TABLE IF NOT EXISTS news (
    data TEXT,
    id TEXT NOT NULL PRIMARY KEY
)""")
