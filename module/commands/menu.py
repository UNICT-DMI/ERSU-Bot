""" /menu command """
from telegram import Update
from telegram.ext import CallbackContext

def menu(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(chat_id=update.message.chat_id, text="") #it will send the current menu based on time, WIP
    pass
