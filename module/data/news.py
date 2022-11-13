import sqlite3
from .constants import DB_PATH

class News:
    def setup(self) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS news(
                Timestamp_UTC DATETIME DEFAULT CURRENT_TIMESTAMP,
                Link TEXT PRIMARY KEY
            )""")

    def insert_new_link(self, link: str) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO news
            (link) values(?)
            """, (link, ))