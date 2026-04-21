"""Data storage and constants"""

from ..scraper.scraper import setup_articles
from .constants import (
    ANSWER_TO_REPORT_TEXT,
    CHECK,
    CONTACT_ERSU,
    CROSS,
    DAYS,
    DAYS_MEAL_REGEX,
    DAYS_TRANSLATION,
    DB_PATH,
    EMPTY,
    ERSU_LINK_REGEX,
    FAQ,
    HELP,
    HELP_CMD_TEXT,
    MEALS,
    MENU_MENSA,
    MENU_SETTINGS,
    REPORT,
    START_CMD_TEXT,
    SYMBOLS,
    UFFICIO_ERSU_CMD_TEXT,
    USER_EMPTY_SETTINGS,
    VALID_DAYS,
    VALID_MEALS,
)
from .news import News
from .user_settings import UserSettings


def setup_db() -> None:
    UserSettings().setup()
    News().setup()
    setup_articles()
