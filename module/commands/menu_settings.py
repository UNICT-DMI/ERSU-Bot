""" /menu_settings command """
from telegram import Update
from telegram.ext import CallbackContext
from module.data.user_settings import UserSettings
from module.data.menu_settings_buttons import generate_keyboard


def menu_settings(update: Update, _: CallbackContext) -> None:
    menu_set = UserSettings()
    settings = menu_set.get_user_settings(update.message.chat_id)

    keyboard = generate_keyboard(settings)
    update.message.reply_text("Imposta quando ricevere il menù:", reply_markup=keyboard)
