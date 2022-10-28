"""/start command"""
import telegram
from telegram import Update
from telegram.ext import CallbackContext
from module.data.constants import START_CMD_TEXT
from module.data.constants import keyboard

def start(update: Update, context: CallbackContext) -> None:
    """Called by the /start command.
    Sends a welcome message

    Args:
        update: update event
        context: context passed by the handler
    """

    reply_keyboard = telegram.ReplyKeyboardMarkup(keyboard,resize_keyboard=True,)
    context.bot.sendMessage(chat_id=update.message.chat_id, text=START_CMD_TEXT, reply_markup=reply_keyboard)
