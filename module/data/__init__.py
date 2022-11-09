"""Data storage and constants"""
from .user_settings import UserSettings

def setupDB() -> None:
    UserSettings().setup()