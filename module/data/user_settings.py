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

        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            temp_cur = cur.execute(f"""SELECT {day}
            FROM user_settings
            WHERE chat_id = {chat_id}
            """)
            old_meal = (temp_cur.fetchall())[0]

            """
            0 = no lunch, no dinner
            1 = only lunch
            2 = only dinner
            3 = lunch and dinner

            accepted values are 1 or 2, 0 and 3 are auto setted
            """

            if old_meal[0] >= 0 and old_meal[0] <= 2 and old_meal[0] != meal:
                cur.execute(f"""UPDATE user_settings
                SET {day} = {day} + {meal}
                WHERE {chat_id} = chat_id
                """)
            elif old_meal[0] == meal or old_meal[0] == 3:
                cur.execute(f"""UPDATE user_settings
                SET {day} = {day} - {meal}
                WHERE {chat_id} = chat_id
                """)

            """
                If the new value is 0 check if all other values are set to 0 and if yes he delete the record
            """

            temp_cur = cur.execute(f"""SELECT {day}
            FROM user_settings
            WHERE {chat_id} = chat_id
            """)
            new_meal = (temp_cur.fetchall())[0]
            if new_meal[0] == 0:
                cur.execute(f"""DELETE FROM user_settings
                WHERE {chat_id} = chat_id
                AND lunedi = 0
                AND martedi = 0
                AND mercoledi = 0
                AND giovedi = 0
                AND venerdi = 0
                AND sabato = 0
                AND domenica = 0
                """)
