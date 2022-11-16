"""Database class"""
import sqlite3
import re
import hashlib
from .constants import DB_PATH, ERSU_LINK_REGEX

class News:
    """
        A class to easy access the database and storing all news link
    """
    def setup(self) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS news(
                Timestamp_UTC DATETIME DEFAULT CURRENT_TIMESTAMP,
                Link TEXT PRIMARY KEY
            )""")

    def is_valid_link(self, link: str) -> bool:
        return bool(re.match(ERSU_LINK_REGEX, link))

    def insert_new_link(self, link: str) -> None:
        if self.is_valid_link(link):
            hash_str = hashlib.new('sha256')
            hash_str.update(link.encode())
            hashed_link = hash_str.hexdigest()

            with sqlite3.connect(DB_PATH) as con:
                cur = con.cursor()
                cur.execute("""INSERT INTO news
                (link) values(?)
                """, (hashed_link, ))
        else:
            raise ValueError("Not a valid link")
