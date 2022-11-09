import sqlite3
from typing import Literal
from .constants import DB_PATH

DAYS = Literal['lunedi', 'martedi', 'mercoledi', 'mercoledi', 'giovedi', 'venerdi', 'sabato', 'domenica']
VALID_DAYS = ('lunedi', 'martedi', 'mercoledi', 'mercoledi', 'giovedi', 'venerdi', 'sabato', 'domenica')

class UserSettings:
    row_factory = lambda cursor, row: row if len(row) != 1 else row[0]

    def setup(self) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS user_settings (
                chat_id TEXT PRIMARY KEY,
                lunedi INTEGER(2) NOT NULL DEFAULT 0,
                martedi INTEGER(2) NOT NULL DEFAULT 0,
                mercoledi INTEGER(2) NOT NULL DEFAULT 0,
                giovedi INTEGER(2) NOT NULL DEFAULT 0,
                venerdi INTEGER(2) NOT NULL DEFAULT 0,
                sabato INTEGER(2) NOT NULL DEFAULT 0,
                domenica INTEGER(2) NOT NULL DEFAULT 0
                )
            """)

    def getUsers(self) -> list:
        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = self.row_factory
            cur = con.cursor()
            res = cur.execute("""SELECT chat_id
            FROM user_settings
            """)
            return res.fetchall()

    def getUserToNofify(self, day: DAYS, meal: int) -> list[str]:
        if meal != 1 and meal != 2:
            raise ValueError("Expected meal to be 1 or 2")
        if day not in VALID_DAYS:
            raise ValueError("Parameter day must be a valid day")

        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = self.row_factory
            cur = con.cursor()
            result = cur.execute(f"""SELECT chat_id
            FROM user_settings
            WHERE {day} = 3 OR {day} = {meal}
            """)
            return result.fetchall()


    def insert_user(self, chat_id:int) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user_settings (chat_id) values (?)", (chat_id, ))


    def setMeal(self, chat_id: int, day: DAYS, meal: int) -> None:
        if meal != 1 and meal != 2:
            raise ValueError("Expected meal to be 1 or 2")
        if day not in VALID_DAYS:
            raise ValueError("Parameter day must be a valid day")