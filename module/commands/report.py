"""/report command"""

from telegram import Update
from telegram.ext import CallbackContext


def report(update: Update, context: CallbackContext) -> None:
    """Called by the /report command.
    Allows the user to send a report to the admins

    Args:
        update: update event
        context: context passed by the handler
    """
    pass
