"""Data storage and constants"""
from .user_settings import UserSettings

def setup_db() -> None:
    UserSettings().setup()