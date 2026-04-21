"""All the commands the bot will react to"""

from .faq import faq_cmd
from .help import help_cmd
from .menu import menu
from .menu_settings import menu_settings
from .reply import reply
from .report import report
from .start import start
from .ufficio_ersu import ufficio_ersu

__all__ = [
    "faq_cmd",
    "help_cmd",
    "menu",
    "menu_settings",
    "reply",
    "report",
    "start",
    "ufficio_ersu",
]
