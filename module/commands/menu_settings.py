""" /menu_settings command """
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, ContextTypes
from module.data.user_settings import UserSettings
from module.data.constants import DB_PATH
from module.data.constants import CROSS, CHECK

def generate_keyboard(chat_id: int) -> list:
    menu_sett = UserSettings()
    settings = (menu_sett.get_user_settings(chat_id))
    keyboard = [
        [
            InlineKeyboardButton("Giorni", callback_data = "0"),
            InlineKeyboardButton("Pranzo", callback_data = "0"),
            InlineKeyboardButton("Cena", callback_data = "0")
        ],

        [
            InlineKeyboardButton("Lunedì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[1] == 0 else CHECK, callback_data = "monday_lunch"),
            InlineKeyboardButton(CROSS if settings[2] == 0 else CHECK, callback_data = "monday_dinner")
        ],

        [
            InlineKeyboardButton("Martedì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[3] == 0 else CHECK, callback_data = "tuesday_lunch"),
            InlineKeyboardButton(CROSS if settings[4] == 0 else CHECK, callback_data = "tuesday_dinner")
        ],

        [
            InlineKeyboardButton("Mercoledì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[5] == 0 else CHECK, callback_data = "wednesday_lunch"),
            InlineKeyboardButton(CROSS if settings[6] == 0 else CHECK, callback_data = "wednesday_dinner")
        ],

        [
            InlineKeyboardButton("Giovedì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[7] == 0 else CHECK, callback_data = "thursday_lunch"),
            InlineKeyboardButton(CROSS if settings[8] == 0 else CHECK, callback_data = "thursday_dinner")
        ],

        [
            InlineKeyboardButton("Venerdì", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[9] == 0 else CHECK, callback_data = "friday_lunch"),
            InlineKeyboardButton(CROSS if settings[10] == 0 else CHECK, callback_data = "friday_dinner")
        ],

        [
            InlineKeyboardButton("Sabato", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[11] == 0 else CHECK, callback_data = "saturday_lunch"),
            InlineKeyboardButton(CROSS if settings[12] == 0 else CHECK, callback_data = "saturday_dinner")
        ],

        [
            InlineKeyboardButton("Domenica", callback_data = "0"),
            InlineKeyboardButton(CROSS if settings[13] == 0 else CHECK, callback_data = "sunday_lunch"),
            InlineKeyboardButton(CROSS if settings[14] == 0 else CHECK, callback_data = "sunday_dinner")
        ],

        [
            InlineKeyboardButton("Azzera", callback_data = "delete_user"),
            InlineKeyboardButton("Chiudi", callback_data = "close_settings")
        ]
    ]
    return keyboard


def menu_settings(update: Update, context: CallbackContext) -> None:
    menu_set = UserSettings()
    menu_set.insert_user(update.message.chat_id)
    keyboard = generate_keyboard(update.message.chat_id)

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Imposta quando ricevere il menù:", reply_markup=reply_markup)