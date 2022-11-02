"""/help command"""
from telegram import Update
from telegram.ext import CallbackContext
from module.data.constants import HELP_CMD_TEXT

def help_cmd(update: Update, context: CallbackContext) -> None:
    """Called by the /help command.
    Shows the help message to the user, explaining what the bot can do

    Args:
        update: update event
        context: context passed by the handler
    """
    context.bot.sendMessage(chat_id=update.message.chat_id, text=HELP_CMD_TEXT)
    