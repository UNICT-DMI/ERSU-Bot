"""Data storage and constants"""
from .user_settings import UserSettings
from .news import News
from .constants import (
    SYMBOLS,
    EMPTY,
    USER_EMPTY_SETTINGS,
    VALID_DAYS,
    DAYS_TRANSLATION,
    DB_PATH,
    CHECK,
    CONTACT_ERSU,
    CROSS,
    DAYS,
    DAYS_MEAL_REGEX,
    ERSU_LINK_REGEX,
    HELP,
    HELP_CMD_TEXT,
    ANSWER_TO_REPORT_TEXT,
    FAQ,
    MEALS,
    MENU_MENSA,
    MENU_SETTINGS,
    REPORT,
    START_CMD_TEXT,
    UFFICIO_ERSU_CMD_TEXT,
    VALID_MEALS,
)


def setup_db() -> None:
    UserSettings().setup()
    News().setup()
