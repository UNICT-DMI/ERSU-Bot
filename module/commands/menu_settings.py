""" /menu_settings command """
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
from module.data.user_settings import UserSettings
from module.data.menu_settings_buttons import generate_keyboard

def menu_settings(update: Update, _: CallbackContext) -> None:
    menu_set = UserSettings()
    menu_set.insert_user(update.message.chat_id)
    settings = menu_set.get_user_settings(update.message.chat_id)

    keyboard = generate_keyboard(settings)
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Imposta quando ricevere il menù:", reply_markup = reply_markup)
