"""/ufficioersu command"""

from telegram import Update
from telegram.ext import CallbackContext
from module.data.constants import UFFICIO_ERSU_CMD_TEXT


def ufficio_ersu(update: Update, context: CallbackContext) -> None:
    """Called by the /ufficioersu command.
    Sends the Ersu office contacts

    Args:
        update: update event
        context: context passed by the handler
    """
    context.bot.sendMessage(chat_id=update.message.chat_id, text=UFFICIO_ERSU_CMD_TEXT)
