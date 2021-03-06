"""Database class"""
import sqlite3
from .constants import DB_PATH, DAYS, MEALS, VALID_DAYS, VALID_MEALS, USER_EMPTY_SETTINGS


class UserSettings:
    """
    A class to easy access the database and storing all user preferences
    """

    def row_factory(self, _, row) -> list:
        return row if len(row) != 1 else row[0]

    def setup(self) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute(
                """CREATE TABLE IF NOT EXISTS user_settings (
                chat_id INTEGER PRIMARY KEY,
                monday_lunch INTEGER(1) NOT NULL DEFAULT 0 CHECK (monday_lunch IN (0, 1)),
                monday_dinner INTEGER(1) NOT NULL DEFAULT 0 CHECK (monday_dinner IN (0, 1)),

                tuesday_lunch INTEGER(1) NOT NULL DEFAULT 0 CHECK (tuesday_lunch IN (0, 1)),
                tuesday_dinner INTEGER(1) NOT NULL DEFAULT 0 CHECK (tuesday_dinner IN (0, 1)),

                wednesday_lunch INTEGER(1) NOT NULL DEFAULT 0 CHECK (wednesday_lunch IN (0, 1)),
                wednesday_dinner INTEGER(1) NOT NULL DEFAULT 0 CHECK (wednesday_dinner IN (0, 1)),

                thursday_lunch INTEGER(1) NOT NULL DEFAULT 0 CHECK (thursday_lunch IN (0, 1)),
                thursday_dinner INTEGER(1) NOT NULL DEFAULT 0 CHECK (thursday_dinner IN (0, 1)),

                friday_lunch INTEGER(1) NOT NULL DEFAULT 0 CHECK (friday_lunch IN (0, 1)),
                friday_dinner INTEGER(1) NOT NULL DEFAULT 0 CHECK (friday_dinner IN (0, 1)),

                saturday_lunch INTEGER(1) NOT NULL DEFAULT 0 CHECK (saturday_lunch IN (0, 1)),
                saturday_dinner INTEGER(1) NOT NULL DEFAULT 0 CHECK (saturday_dinner IN (0, 1)),

                sunday_lunch INTEGER(1) NOT NULL DEFAULT 0 CHECK (sunday_lunch IN (0, 1)),
                sunday_dinner INTEGER(1) NOT NULL DEFAULT 0 CHECK (sunday_dinner IN (0, 1))
                )"""
            )

    def set_meal(self, chat_id: int, day: DAYS, meal: MEALS) -> None:
        if day not in VALID_DAYS:
            raise ValueError("Parameter day must be a valid day")
        if meal not in VALID_MEALS:
            raise ValueError("Expected meal to be lunch or dinner")

        day_meal = f"{day}_{meal}"

        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute(
                f"INSERT INTO user_settings (chat_id, {day_meal}) values (?, 1)"
                f"ON CONFLICT(chat_id) DO UPDATE SET {day_meal} = 1 - user_settings.{day_meal}",
                (chat_id,),
            )

    def get_users(self) -> list[int]:
        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = self.row_factory
            cur = con.cursor()
            result = cur.execute(
                """SELECT chat_id
            FROM user_settings
            """
            )
            return result.fetchall()

    def get_user_settings(self, chat_id: int) -> list[int]:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            result = cur.execute(
                """SELECT *
            FROM user_settings
            WHERE chat_id = (?)
            """,
                (chat_id,),
            )
            settings = result.fetchone()
            return settings[1:] if settings else USER_EMPTY_SETTINGS

    def get_users_to_notify(self, day: DAYS, meal: MEALS) -> list[int]:
        if day not in VALID_DAYS:
            raise ValueError("Parameter day must be a valid day")
        if meal not in VALID_MEALS:
            raise ValueError("Expected meal to be lunch or dinner")

        day_meal = f"{day}_{meal}"

        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = self.row_factory
            cur = con.cursor()
            result = cur.execute(
                """SELECT chat_id
            FROM user_settings
            WHERE (?) = 1
            """,
                (day_meal,),
            )
            return result.fetchall()

    def delete_user(self, chat_id: int) -> None:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute(
                """DELETE FROM user_settings
                WHERE chat_id = (?)
                """,
                (chat_id,),
            )
