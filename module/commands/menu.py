""" /menu command """
from telegram import Update
from telegram.ext import CallbackContext

def menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("") #it will send the current menu based on time, WIP
    return