"""Database class"""
import sqlite3
from .constants import DB_PATH
from .constants import DAYS, MEALS, VALID_DAYS, VALID_MEALS

"""A class to easy access the database and storing all user preferences"""
class UserSettings:
    def row_factory(self, cursor, row) -> list:
        return row if len(row) != 1 else row[0]

    def setup(self) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS user_settings (
                chat_id INTEGER PRIMARY KEY,
                monday_lunch INTEGER(1) NOT NULL DEFAULT 1,
                monday_dinner INTEGER(1) NOT NULL DEFAULT 0,

                tuesday_lunch INTEGER(1) NOT NULL DEFAULT 1,
                tuesday_dinner INTEGER(1) NOT NULL DEFAULT 0,

                wednesday_lunch INTEGER(1) NOT NULL DEFAULT 1,
                wednesday_dinner INTEGER(1) NOT NULL DEFAULT 0,

                thursday_lunch INTEGER(1) NOT NULL DEFAULT 1,
                thursday_dinner INTEGER(1) NOT NULL DEFAULT 0,

                friday_lunch INTEGER(1) NOT NULL DEFAULT 1,
                friday_dinner INTEGER(1) NOT NULL DEFAULT 0,

                saturday_lunch INTEGER(1) NOT NULL DEFAULT 0,
                saturday_dinner INTEGER(1) NOT NULL DEFAULT 0,

                sunday_lunch INTEGER(1) NOT NULL DEFAULT 0,
                sunday_dinner INTEGER(1) NOT NULL DEFAULT 0
                )""")

    def insert_user(self, chat_id:int) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("""SELECT chat_id
            FROM user_settings
            WHERE chat_id = (?)""", (chat_id, ))

            user_exists = cur.fetchall()
            if len(user_exists) == 0:
                cur.execute("INSERT INTO user_settings (chat_id) values (?)", (chat_id, ))

    def set_meal(self, chat_id: int, day: DAYS, meal: MEALS) -> None:
        if day not in VALID_DAYS:
            raise ValueError("Parameter day must be a valid day")
        if meal not in VALID_MEALS:
            raise ValueError("Expected meal to be lunch or dinner")

        day_meal = day + '_' + meal

        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute(f"""SELECT {day_meal}
            FROM user_settings
            WHERE chat_id = {chat_id}
            """)
            old_meal = cur.fetchall()

            if old_meal == [(0, )]:
                cur.execute(f"""UPDATE user_settings
                SET {day_meal} = 1
                WHERE chat_id = {chat_id}
                """)
            if old_meal == [(1, )]:
                cur.execute(f"""UPDATE user_settings
                SET {day_meal} = 0
                WHERE chat_id = {chat_id}
                """)

    def get_users(self) -> list[int]:
        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = self.row_factory
            cur = con.cursor()
            result = cur.execute("""SELECT chat_id
            FROM user_settings
            """)
            return result.fetchall()

    def get_user_settings(self, chat_id: int) -> list:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            result = cur.execute("""SELECT *
            FROM user_settings
            WHERE chat_id = (?)
            """, (chat_id, )
            )
            tmp = (result.fetchall())[0]
            settings = [tmp[var+1] for var in range(14)]
            return settings

    def get_users_to_notify(self, day: DAYS, meal: MEALS) -> list[int]:
        if day not in VALID_DAYS:
            raise ValueError("Parameter day must be a valid day")
        if meal not in VALID_MEALS:
            raise ValueError("Expected meal to be lunch or dinner")

        day_meal = day + '_' + meal

        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = self.row_factory
            cur = con.cursor()
            result = cur.execute("""SELECT chat_id
            FROM user_settings
            WHERE (?) = 1
            """, (day_meal, ))
            return result.fetchall()

    def delete_user(self, chat_id: int) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("""DELETE FROM user_settings
                WHERE chat_id = (?)
                """, (chat_id, ))

    def reset_user_settings(self, chat_id: int) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("""REPLACE INTO user_settings
            values ((?), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)""", (chat_id, ))
