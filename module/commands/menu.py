""" /menu command """
from telegram import Update
from telegram.ext import CallbackContext

def menu(update: Update, context: CallbackContext) -> None:
    # pylint: disable=line-too-long
    context.bot.sendMessage(chat_id=update.message.chat_id, text="Questa funzione non è ancora disponibile") # it will send the current menu based on time, WIP
