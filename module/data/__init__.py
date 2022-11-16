"""Data storage and constants"""
from .user_settings import UserSettings
from .news import News

def setup_db() -> None:
    UserSettings().setup()
    News().setup()
