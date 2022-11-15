""" /menu command """
from telegram import Update
from telegram.ext import CallbackContext

from module.data.menu_updater import update_menu

def menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("") #it will send the current menu based on time, WIP
    return